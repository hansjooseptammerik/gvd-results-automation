import json
import os
from typing import Any, Dict
import requests

def update_shop_metafield_json(
    payload: Dict[str, Any],
    shop: str,
    token: str,
    namespace: str = "custom",
    key: str = "gvd_stats_json",
    api_version: str = "2025-01",
) -> None:
    if shop.startswith("https://"):
        shop = shop.replace("https://", "")
    if shop.endswith("/"):
        shop = shop[:-1]

    base = f"https://{shop}/admin/api/{api_version}"
    headers = {
        "X-Shopify-Access-Token": token,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    params = {"namespace": namespace, "key": key}
    r = requests.get(f"{base}/metafields.json", headers=headers, params=params, timeout=30)
    r.raise_for_status()
    mf_list = (r.json() or {}).get("metafields") or []

    value = json.dumps(payload, ensure_ascii=False)

    if mf_list:
        mf_id = mf_list[0]["id"]
        body = {"metafield": {"id": mf_id, "value": value, "type": "json"}}
        u = requests.put(f"{base}/metafields/{mf_id}.json", headers=headers, data=json.dumps(body), timeout=30)
        u.raise_for_status()
    else:
        body = {"metafield": {"namespace": namespace, "key": key, "type": "json", "value": value}}
        c = requests.post(f"{base}/metafields.json", headers=headers, data=json.dumps(body), timeout=30)
        c.raise_for_status()

def maybe_update_shopify(payload: Dict[str, Any]) -> bool:
    shop = os.getenv("SHOPIFY_SHOP")
    token = os.getenv("SHOPIFY_TOKEN")

    if not shop or not token:
        print("[shopify] Missing SHOPIFY_SHOP or SHOPIFY_TOKEN. Skipping Shopify update.")
        return False

    namespace = os.getenv("SHOPIFY_NAMESPACE", "custom")
    key = os.getenv("SHOPIFY_KEY", "gvd_stats_json")
    api_version = os.getenv("SHOPIFY_API_VERSION", "2025-01")

    update_shop_metafield_json(payload, shop=shop, token=token, namespace=namespace, key=key, api_version=api_version)
    print(f"[shopify] Updated metafield {namespace}.{key} on {shop}")
    return True
