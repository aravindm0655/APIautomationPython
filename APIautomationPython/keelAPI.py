import requests
import json

base_url="https://keel-api-dev.talentship.io/api"

b1= {
    "user_name" : "admin",
    "password": "Admin@123"
}

# This API use for Super Admin login. 
def post1Request():
    url=base_url+ "/login" 
    
    res1=requests.post(url, data=b1)
    assert res1.status_code==200, "Login Failed "
    resp= res1.json()
    # response= json.dumps(resp ,indent=4)
    # print(response)
    token =resp['access_token']
    print(".......POST REQUEST IS DONE.......")
    print(".......=====================.......\n\n")
    return token


# This API use for Adding Organization by giving unique name 
def addOrganization(token1):
    url =base_url+ "/addorganization"
    head = {"Authorization": f"Bearer {token1}"}
    with open("load.json", "r") as json_file:   
        json_data = json.load(json_file)
    res2 = requests.post(url, json=json_data, headers=head)
    assert res2.status_code==200, "Creation Failed "
    resp= res2.json()
    # response= json.dumps(resp ,indent=4)
    global appkey
    appkey=resp['data']['result']['organization']['appKey']
    # print(response)
    print(".......ADD ORGANIZATION  IS DONE.......")
    print(".......=====================.......\n\n")
    
    return head
    
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
    # assert res4.status_code==200, "Get Request Failed "
    # resp=res4.json()
    # response= (json.dumps(resp , indent=4))
    # print(response)
    
    print(".......DISPLAY REQUEST IS DONE.......")
    print(".......=====================.......\n\n")

# # This API is use for to check Availability of domain while creating organization
# def domainRequest():
#     url=base_url+ "/checkdomain?domain="
    


token1 =post1Request()
head=addOrganization(token1)
getRequest()
listdb()