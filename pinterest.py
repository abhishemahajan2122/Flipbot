from apify_client import ApifyClient
client = ApifyClient("apify_api_aZ16PlpIOTcCOTvnuzOapIAzmXTBdM0yRzyS")
run_input = {
    "startUrls": [
        "Fasheditorials",
    ],
    "maxPinsCnt": 10,
    "proxyConfig": {"useApifyProxy": True}
}

run = client.actor("alexey/pinterest-crawler").call(run_input=run_input)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
