import requests
import pandas as pd

# Test with a sample public API (JSONPlaceholder)
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
data = response.json()

# Convert to DataFrame just to test pandas
df = pd.DataFrame(data)

# Show first 5 rows
print(df.head())