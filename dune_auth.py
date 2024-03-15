from dotenv import load_dotenv
import os
import requests
from dune_client.client import DuneClient

load_dotenv('.secrets')

# Fetch the DUNE_KEY environment variable
dune_key = os.getenv('DUNE_KEY')

dune = DuneClient(dune_key)
query_result = dune.get_latest_result(3507935)
print(query_result.result)