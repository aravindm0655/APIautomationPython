import requests
import json

base_url="https://keel-api-dev.talentship.io/api"

b1={
    "firstName": "super",
    "lastName": "admin",
    "userName":"admin",
    "email":"admin@123",
    "password": "Admin@123"
}
# This API use for create Super Admin
def createRequest():
    url=base_url+"/adminusers/create"
    res1=requests.post(url, data=b1)
    resp=res1.json()
    response= json.dumps(resp ,indent=4)
    print(response)
    
createRequest()
