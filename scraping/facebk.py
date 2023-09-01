from apify_client import ApifyClient

# Initialize the ApifyClient with your API token
client = ApifyClient("apify_api_aZ16PlpIOTcCOTvnuzOapIAzmXTBdM0yRzyS")

# Prepare the Actor input
run_input = { "startUrls": [
        { "url": "https://www.facebook.com/groups/2244851022322509/?hoisted_section_header_type=recently_seen&multi_permalinks=2623561577784783" },
        { "url": "https://www.facebook.com/HiltonGardenInnMontrealAirport/" },
    ] }

# Run the Actor and wait for it to finish
run = client.actor("apify/facebook-pages-scraper").call(run_input=run_input)

# Fetch and print Actor results from the run's dataset (if there are any)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
