import requests
import json
from jsonpath import jsonpath

headers={}
token="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"
#headers["Accept"] = "application/json"
#headers["Authorization"] = "Bearer {token}"
headers["Authorization"] = "Bearer " + token
res = requests.get("https://api.github.com/user",headers=headers)
print(res.json())

# out = res.json()
# loginname=jsonpath(out,)
# print(loginname)