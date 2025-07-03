# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://veeramallaabhishek.atlassian.net/rest/api/3/project"     #replace with your own email

API_TOKEN=""    #paste api token created on jira dashboard

auth = HTTPBasicAuth("", API_TOKEN)  #use your email address

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)

name = output[0]["name"]     #it will print the name of first project 

print(name)