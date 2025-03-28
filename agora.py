import requests
import json

url = "http://localhost:8000/delete_cadastro/3"

payload = json.dumps({
  "name": "José"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("PATCH", url, headers=headers, data=payload)

print(response.text)


