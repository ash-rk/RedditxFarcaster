from dotenv import load_dotenv
import os
from dune_client.client import DuneClient
from dune_client.query import QueryBase

load_dotenv('.secrets')

# Fetch the DUNE_KEY environment variable
dune_key = os.getenv('DUNE_KEY')

query = QueryBase(
    name="All Farcaster Channels",
    query_id=3528724
)

dune = DuneClient(dune_key)

results_csv = dune.run_query_csv(query)
with open('../data_retrieved/query_results.csv', 'wb') as file:
    file.write(results_csv.data.getvalue())

# query2 = QueryBase(
#     name="All Farcaster User Channel Details",
#     query_id=3534411
# )

# user_channel_metrics = dune.run_query_csv(query2)
# with open('user_channel_metrics.csv', 'wb') as file:
#     file.write(user_channel_metrics.data.getvalue())