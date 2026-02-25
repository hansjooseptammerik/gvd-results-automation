# GVD Darts Results Automation

See projekt loeb Sofascore'ist Gian van Veeni viimaseid 6 tulemust ja 6 järgmist mängu ning saadab info Shopify poodi metafieldi, kui token on olemas. Kui token puudub, salvestab info `output/gvd_stats.json` faili.

## Lokaalne käivitamine

1. `pip install -r requirements.txt`
2. Lisa `.env` fail keskkonnamuutujatega kui vaja (või kasuta keskkonnamuutujaid otse).
3. Käivita:
   ```
   python src/main.py
   ```
## GitHub Actions automaatsus

- Jookseb igal öösel Eesti aja järgi südaööl.

## Vajalikud keskkonnamuutujad

- PLAYER_NAME (nt. Gian van Veen)
- SHOPIFY_SHOP (kui vaja)
- SHOPIFY_TOKEN (kui vaja)
- SHOPIFY_NAMESPACE (valikud: custom, ... või oma metafieldi namespace)
- SHOPIFY_KEY (valikuline, default: gvd_stats_json)
- SHOPIFY_API_VERSION (default: 2025-01)

## Struktuur

- src/main.py - põhiskript
- src/sofascore_scraper.py - Sofascore'ist lugemine
- src/shopify_update.py - Shopify andmeülekanne
- output/gvd_stats.json - väljundfail (iga jooksuga üle kirjutatakse)
