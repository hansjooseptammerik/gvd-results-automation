# Gian van Veen darts stats automation

See projekt scrapib Sofascore’ist Gian van Veeni viimased ja tulevased darts-mängud iga päev ning salvestab need JSON failina; kui Shopify tokenid lisatakse, laeb automaatselt Shopify metafieldi.

## Paigaldus

- Nõuab Chrome’i ja Chromedriverit serveris/runneris (GitHub Actions script teeb seda).
- Lokaalselt installi:
    pip install -r requirements.txt
    python src/main.py

## Käsitsi käivitamine

- GitHub Actions > Daily GVD update (SofaScore) > Run workflow

## Võtmed:
- Shopify tokenid pole kohustuslikud; kui puudu, salvestab ainult JSON.
- Scrapingu loogika töötab Seleniumi päris Chrome brauseriga (headless).

## Failid:
- .github/workflows/daily.yml – GitHub Actions töövoog
- requirements.txt
- src/sofascore_scraper.py
- src/main.py
- src/shopify_update.py
