import requests
import datetime
import os
import json

cookies = {
    '_ga': 'GA1.1.813394280.1764340212',
    'FCCDCF': '%5Bnull%2Cnull%2Cnull%2C%5B%22CQbmPwAQbmPwAEsACBETCHFoAP_gAEPgAA6ILUEB5C5GTSFBYTZ1KMsEYAAHwRgAJsAgAgYBgwABQJKU5JwCBGAAEAhIhiICmAAAKlSBIAFAGBAQAAAAAAAAIAAEIAQQgAAIJCAAAAABAABICAAoAYoAEAAAwDiEBAUAkBgMQNIISNyQCQAABSCAQgAAEACAAQAAAFhgIAAA4AAAUGgEEIBAWAAAEEEYABnshAAoIAggABAQQAgAACQCRQACgCAAFDQgABAMAAgAAgwABACAAEAEFqCA8hciJpCgsBgqkGWCEAAL4IwAE2AQAAMAwYAAoElKckYBCjAAAAQEABEADAAAESoAkACADAwAAAAAAAAAEAASAAIIQAAEEBAAABAAgAAgAAAEAMUACAAAYBQCAgKAQIQGIGkAJC5IBIAQApBAIEAACABAAIAAACQwEAAAcAAAKDAACEAgLAAACAAIAAz2QgAQEAAAAEgAIAQAABIRIgABAAAAChoQAAAEAAQAAQYAAgBAACACAAA.dngACAAAAAA%22%2C%222~55.70.89.108.135.147.149.161.184.211.259.272.313.314.358.385.415.442.486.540.621.938.981.1029.1031.1033.1046.1067.1092.1097.1126.1205.1268.1301.1329.1514.1516.1558.1579.1584.1598.1616.1651.1697.1716.1753.1782.1810.1832.1859.1917.1985.1987.2068.2069.2140.2224.2271.2282.2316.2328.2331.2373.2387.2440.2501.2567.2571.2572.2575.2577.2628.2629.2642.2646.2650.2657.2677.2767.2778.2822.2860.2878.2887.2889.2898.2922.2970.3100.3169.3182.3190.3194.3215.3226.3234.3290.3292.3300.3330.3331.4631.10631.14332.28031.29631.45931~dv.%22%2C%22FE0B62FC-5F8C-4225-9893-4AD16BECFCEF%22%5D%2Cnull%2Cnull%2C%5B%5B32%2C%22%5B%5C%224b2bed0c-6701-4783-8051-3679b1d8e8a0%5C%22%2C%5B1764340208%2C624000000%5D%5D%22%5D%5D%5D',
    'AD_VERGE_SESSION_COOKIE_V1': '6e6f16d7-51ec-4ee5-8cd6-4ecf87730070',
    '_li_dcdm_c': '.sofascore.com',
    'cto_bundle': 'ScYlLV9FS3M4ZGh0VXh1MEdnJTJGb1hQVDFtZFdtZ2pyNE92OVpScDElMkZsYU16QUFQektBT25aRmZ1VGE1QW9IR1BwQlIyZFdUakk5dWJrcWxDUzg5JTJCVkllVmRlb1BwMkljWHlnNUVoR05mJTJCVnNDVmEzRXdCaHZhNWpoaWwlMkZsaUVteDNlTVpyYW1sMzRPeklLWWE3a1p6ayUyQlRFWnclM0QlM0Q',
    'FCNEC': '%5B%5B%22AKsRol9hcTW5UvC4V0jbHcKJaijWzxMZHlkIg7ML8YnF942GM6YZ0RO5_ixloBze6E2puPWXPfljxktQrM8lugXhdcmJVRnpRwOKQmEqNFD7VnbK7quLGCajB-RN3qd-gY64ZKWQ-tOpY_9Sm-JW9cXgC1q1uP-W_w%3D%3D%22%5D%5D',
    '__gads': 'ID=43268125400989bd:T=1764340218:RT=1772103012:S=ALNI_MY5bhdqbu3zTfPuM0G7idQuU2Pxlg',
    '__gpi': 'UID=000012940d7f4bf0:T=1764340218:RT=1772103012:S=ALNI_MbKB_8FydXG-b0bWC7VhA356-212w',
    '__eoi': 'ID=642a1b27a9a96a6f:T=1764340218:RT=1772103012:S=AA-Afjbkt7dn1kwiIhfyoV7xQkDf',
    '_ga_HNQ9P9MGZR': 'GS2.1.s1772094281$o6$g1$t1772103064$j42$l0$h0',
}

headers = {
    'accept': '*/*',
    'accept-language': 'et-EE,et;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'if-none-match': 'W/"e6d872ab74"',
    'priority': 'u=1, i',
    'referer': 'https://www.sofascore.com/darts/player/van-veen-gian/410446',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Mobile Safari/537.36',
    'x-requested-with': '3de42b',
}

url = 'https://www.sofascore.com/api/v1/team/410446/featured-event'

def fetch_featured_event():
    resp = requests.get(url, cookies=cookies, headers=headers)
    resp.raise_for_status()
    data = resp.json()
    return data

def save_event_to_file(event_data, outpath="output/gvd_featured_event.json"):
    os.makedirs(os.path.dirname(outpath), exist_ok=True)
    out = {
        "scraped_at": datetime.datetime.now().isoformat(),
        "event": event_data.get("featuredEvent", {})
    }
    with open(outpath, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"Saved featured event to {outpath}")

if __name__ == "__main__":
    event_data = fetch_featured_event()
    save_event_to_file(event_data)
