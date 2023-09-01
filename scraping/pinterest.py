from apify_client import ApifyClient

# Initialize the ApifyClient with your API token
client = ApifyClient("apify_api_aZ16PlpIOTcCOTvnuzOapIAzmXTBdM0yRzyS")

# Prepare the Actor input
run_input = {
    "startUrls": [
        "Fasheditorials",
    ],
    "maxPinsCnt": 3,
    "proxyConfig": { "useApifyProxy": True }
}

# Run the Actor and wait for it to finish
run = client.actor("alexey/pinterest-crawler").call(run_input=run_input)

final_list=[]
# Fetch and print Actor results from the run's dataset (if there are any)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    final_list.append(item["image"]["url"])
    # print(item)
    
with open("output.txt", "a") as f:
  # Write the contents of the list to the file
  for item in final_list:
    f.write(item + "\n")