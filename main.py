# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
import os
from dotenv import load_dotenv

load_dotenv()

url = "https://vinted.atlassian.net/rest/api/3/issue/IT-55555"
name = os.environ.get("JIRA_ACCOUNT_EMAIL")
token = os.environ.get("JIRA_ACCOUNT_TOKEN")

auth = HTTPBasicAuth(name, token)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))