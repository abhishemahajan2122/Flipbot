# import pandas as pd

# # Read the CSV file into a Pandas DataFrame
# df = pd.read_csv("Files/generated_data.csv")

# # Get the number of rows to drop
# num_rows_to_drop = 4000

# # Randomly sample the rows to drop
# rows_to_drop = df.sample(num_rows_to_drop, random_state=42)

# # Drop the rows
# df = df.drop(rows_to_drop.index)

# # Save the DataFrame to a CSV file
# df.to_csv("data_dropped.csv", index=False)
import pandas as pd
import random

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv("data_dropped.csv")

# Get the column names
column_names = df.columns.tolist()

# Loop over the columns
str="";
for column_name in ['description','Product Name']:
  # Get the top 5 frequently occuring items
  top_5_items = df[column_name].value_counts().head(5)
  random_number = random.randint(0, 4)
  str += top_5_items.index[random_number] + "\n"

# Print the string
print(str)
with open('final_prompt.txt', 'a') as file:
    file.write(str)
  # Print the top 5 items
#   print(f"Top 5 frequently occuring items in {column_name}:\n{top_5_items}")