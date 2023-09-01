from apify_client import ApifyClient

# Initialize the ApifyClient with your API token
client = ApifyClient("apify_api_aZ16PlpIOTcCOTvnuzOapIAzmXTBdM0yRzyS")

# Prepare the Actor input
run_input = {
    "hashtags": ["fashion","stylemilkshake","clothing"],
    "resultsLimit": 3,
}

# Run the Actor and wait for it to finish
run = client.actor("apify/instagram-hashtag-scraper").call(run_input=run_input)

# Fetch and print Actor results from the run's dataset (if there are any)
list=[]
final_list=[]
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    list.append({
        "caption": item["caption"],
        "hashtags": item["hashtags"]
    })
    final_list.append(item["displayUrl"])
    # print(item)
    # print("\n\n\n\n")
# print(list)

with open("output.txt", "a") as f:
  # Write the contents of the list to the file
  for item in final_list:
    f.write(item + "\n")
