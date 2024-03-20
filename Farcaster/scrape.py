import pandas as pd
import requests
import json

# Adjust the path to the CSV file
df = pd.read_csv('../data_retrieved/cleaned_query_results.csv')

# Prepare a list to hold the data
data_to_save = []

# Loop through the first 10 rows in the DataFrame
for index, row in df.iterrows():
    channel = row['channel']  # Adjusted column name
    url = f"https://client.warpcast.com/v2/channel?key={channel}"
    
    # Fetch the web content
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # Parse the JSON content
            data = json.loads(response.text)
            
            # Extract the followerCount
            follower_count = data.get('result', {}).get('channel', {}).get('followerCount', 'Not found')
            
            # Store the channel and followerCount in the list
            data_to_save.append({"channel": channel, "followers": follower_count})
            
            print(f"{channel} follower: {follower_count}")
        else:
            print(f"Failed to fetch content for row {index}: Status code {response.status_code}")
    except Exception as e:
        print(f"Error fetching content for row {index}: {e}")

# Convert the list of dictionaries into a DataFrame
results_df = pd.DataFrame(data_to_save)

# Save the DataFrame to a CSV file
results_df.to_csv('../data_retrieved/farcaster_channel_followers.csv', index=False)

# Note: The 'index=False' parameter is used to prevent pandas from writing row indices into the CSV file.
