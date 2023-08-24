import requests
import json
from randome import randomdata


base_url="https://keel-api-dev.talentship.io/api"
    
with open("loads.json", "r") as json_file:   
    json_data = json.load(json_file)
b1=randomdata.data1
b2= randomdata.data2
randomdata.generate_data()
# This API use for Super Admin login. 
def post1Request():
    url=base_url+ "/login" 
    
    res1=requests.post(url, data=b1)
    assert res1.status_code==200, "Login Failed "
    resp= res1.json()
    # response= json.dumps(resp ,indent=4)
    # print(response)
    token1 =resp['access_token']
    print(".......POST REQUEST IS DONE.......")
    print(".......=====================.......\n\n")
    head = {"Authorization": f"Bearer {token1}"}
    return head

    
# This API use for Adding Organization by giving unique name 
def addOrganization():
    url =base_url+ "/addorganization"
    res2 = requests.post(url, data=json_data, headers=head)
    print("\n\n",res2,"\n\n")
    resp= res2.json()
    response= json.dumps(resp ,indent=4)
    print(response)
    global appkey
    appkey=resp['data']['result']['organization']['appKey']
    print(".......ADD ORGANIZATION  IS DONE.......")
    print(".......=====================.......\n\n")
    
    return head
    

# This API use for create Super Admin
def createRequest():
    url=base_url+"/adminusers/create"
    res1=requests.post(url, json=b2, headers=head)
    resp=res1.json()
    # response= json.dumps(resp ,indent=4)
    # print(response)
    print("....... SUPER ADMIN CREATED  IS DONE.......")
    print(".......=====================.......\n\n")
    
# This API used for to GET the single Organization data by passing the “appkey”  
def getRequest():
    url=base_url+"/org/" +appkey
    res3=requests.get(url, headers=head)
    assert res3.status_code==200, "Get Request Failed "
    # resp=res3.json()
    # response= (json.dumps(resp , indent=4))
    # print(response)
    print(".......GET REQUEST IS DONE.......")
    print(".......=====================.......\n\n")

# This API use for List all organization present in DB and we get the total count of “records” in response 
def listdb():
    url=base_url+ "/allorganization?page=1&limit=10"
    res4=requests.get(url, headers=head)
    assert res4.status_code==200, "Get Request Failed "
    # resp=res4.json()
    # response= (json.dumps(resp , indent=4))
    # print(response)
    print(".......DISPLAY REQUEST IS DONE.......")
    print(".......=====================.......\n\n")

  


head =post1Request()
addOrganization()
createRequest()
getRequest()
listdb()