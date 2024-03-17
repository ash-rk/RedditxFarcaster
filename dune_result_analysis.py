import pandas as pd
import re

# Define a function to extract channel name from the HTML anchor tag
def extract_channel_name(html_link):
    # Use regular expression to extract the text between > and <
    match = re.search(r'>(.*?)<', html_link)
    return match.group(1) if match else html_link

# Load the CSV data into a pandas DataFrame
df = pd.read_csv('query_results.csv')

# Clean the 'channel' column by applying the function
df['channel'] = df['channel'].apply(extract_channel_name)

# Remove duplicates based on the 'channel' column
df = df.drop_duplicates(subset=['channel'])

# Save the cleaned DataFrame to a new CSV file
cleaned_csv_filename = 'cleaned_query_results.csv'
df.to_csv(cleaned_csv_filename, index=False)

# Display the first few rows of the cleaned DataFrame to check it
print(df.head())

# Display a quick statistical summary of the numerical columns
print(df.describe())
