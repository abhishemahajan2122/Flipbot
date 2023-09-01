from apify_client import ApifyClient

client = ApifyClient("apify_api_aZ16PlpIOTcCOTvnuzOapIAzmXTBdM0yRzyS")
run_input = {"handles": ["diwali"],
             "tweetsDesired": 5, "addUserInfo": True}
run = client.actor("quacker/twitter-scraper").call(run_input=run_input)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
