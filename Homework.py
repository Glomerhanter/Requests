import requests
import json

status = 'available'
headers = {'accept': 'application/json'}
headers1 = {'accept': 'application/json', 'Content-Type': 'application/json'}

params = {'status': 'available'}

info = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}


resget = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}", params=params, headers=headers)
respost = requests.post(f"https://petstore.swagger.io/v2/pet", headers=headers1, data=json.dumps(info, ensure_ascii=False))
resput = requests.put(f"https://petstore.swagger.io/v2/pet", headers=headers1, data=json.dumps(info, ensure_ascii=False))
IdNewPets = info.get("id")
resdelete = requests.delete(f"https://petstore.swagger.io/v2/pet/{IdNewPets}", headers=headers)

print(resget.text)
print(respost.text)
print(resput.text)
