from dotenv import load_dotenv
import os
import requests
from dune_client.client import DuneClient

load_dotenv('.secrets')

# Fetch the DUNE_KEY environment variable
dune_key = os.getenv('DUNE_KEY')

dune = DuneClient(dune_key)
query_result = dune.get_latest_result(3528724)

# Store the output in a text file
with open('query_result.txt', 'w') as file:
    file.write(str(query_result.result))
