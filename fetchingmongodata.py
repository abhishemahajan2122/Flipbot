import pandas as pd
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["your_database_name"]
orders = db["orders"].find()
data = []
for order in orders:
    for product_item in order["products"]:
        product_id = product_item["product"]
        product = db["products"].find_one({"_id": product_id})
        if product:
            data.append({
                "Product Name": product["name"],
                "Product Price": product["price"],
                "Product Count": product_item["count"],
                "description": product["description"],
            })
df = pd.DataFrame(data)
csv_filename = "order_product_details.csv"
df.to_csv(csv_filename, index=False)
print(f"Data exported to {csv_filename}")
