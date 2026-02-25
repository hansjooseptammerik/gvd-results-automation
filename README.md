# GVD Results Automation (SofaScore → JSON → Shopify)

This repo fetches **Gian van Veen** matches from **SofaScore** and generates a JSON payload suitable for a Shopify **Shop metafield (type: JSON)**.

It writes:
- `output/gvd_stats.json`

Payload format:
```json
{
  "last_updated": "YYYY-MM-DD HH:MM",
  "upcoming": [ { ...match... } ],
  "results": [ { ...match... } ]
}
```

## Local run
```bash
pip install -r requirements.txt
python -m playwright install chromium
python src/main.py
```

## GitHub Actions
Workflow: `.github/workflows/daily.yml`
- Runs daily at **22:00 UTC** (≈ **00:00 Estonia time** in winter)
- Uploads the JSON as an artifact

### Enable Shopify update later
Add repo secrets:
- `SHOPIFY_SHOP` = `yourstore.myshopify.com`
- `SHOPIFY_TOKEN` = Admin API access token

Optional secrets:
- `SHOPIFY_NAMESPACE` (default `custom`)
- `SHOPIFY_KEY` (default `gvd_stats_json`)
- `SHOPIFY_API_VERSION` (default `2025-01`)

If secrets are missing, the workflow still generates the JSON and uploads it as an artifact.
