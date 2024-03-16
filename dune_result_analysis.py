import pandas as pd

# Load the CSV data into a pandas DataFrame
df = pd.read_csv('query_results.csv')

# Display the first few rows of the DataFrame to check it
print(df.head())

# Now you can proceed with your analysis using the DataFrame
# For example, you might want to describe the data to get a quick statistical summary of the numerical columns
print(df.describe())
