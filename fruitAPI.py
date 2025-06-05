import requests
import json
import pandas as pd
# Fetch data from the Fruityvice API
data = requests.get("https://web.archive.org/web/20240929211114/https://fruityvice.com/api/fruit/all")
result = json.loads(data.text)  # Convert the response to JSON format
df1 = pd.DataFrame(result)  # Convert the JSON data to a DataFrame
df1
df2 = pd.json_normalize(result)  # Normalize the JSON data to a flat table
df2
df2.to_csv('fruits.csv', index = False)  # Save the DataFrame to a CSV file
# Display the first few rows of the DataFrame       
df2.head()  # Show the first few rows of the DataFrame
cherry = df2.loc[df2["name"] == 'Cherry']
(cherry.iloc[0]['family']) , (cherry.iloc[0]['genus'])

# Display specific fruit information
banana = df2.loc[df2["name"] == 'Banana']
(banana.iloc[0]['family']) , (banana.iloc[0]['genus'])

banana.to_csv('banana.csv', index = False)  # Save banana data to a CSV file

# Display specific fruit information    
mango = df2.loc[df2["name"] == 'Mango']
mango_family = mango.iloc[0]
mango_family.to_csv('mango.csv', index = False)  # Save mango data to a CSV file
# ...existing code...
banana = df2.loc[df2["name"] == 'Banana']
mango = df2.loc[df2["name"] == 'Mango']

# Combine banana and mango rows into one DataFrame
banana_mango = pd.concat([banana, mango])


# Save to a single CSV file
banana_mango.to_csv('banana_mango.csv', index=False)
# ...existing code...
