import json

from jsonpath import jsonpath



import requests

headers={
"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36"

}
response=requests.get('https://www.lagou.com/lbs/getAllCitySearchLabels.json',headers=headers)

# print(response.content.decode())

json_response=json.loads(response.content.decode())

print(json_response)
c=jsonpath(json_response,"$..name")
print(c)
print(len(c))

print()