from apify_client import ApifyClient

# Initialize the ApifyClient with your API token
client = ApifyClient("apify_api_aZ16PlpIOTcCOTvnuzOapIAzmXTBdM0yRzyS")

# Prepare the Actor input
run_input = { "handles": ["fashion","fastytrends"],"tweetsDesired": 3,"addUserInfo": True}

# Run the Actor and wait for it to finish
run = client.actor("quacker/twitter-scraper").call(run_input=run_input)

# Fetch and print Actor results from the run's dataset (if there are any)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
