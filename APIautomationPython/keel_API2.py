import requests
import json


base_url="https://keel-api-dev.talentship.io/api"

b1= {
    "user_name" : "admin",
    "password": "Admin@123"
}
with open("load.json", "r") as json_file:   
    json_data = json.load(json_file)
    
# This API use for Super Admin login. 
def post1Request():
    url=base_url+ "/login" 
    
    res1=requests.post(url, data=b1)
    assert res1.status_code==200, "Login Failed "
    resp= res1.json()
    # response= json.dumps(resp ,indent=4)
    # print(response)
    token1 =resp['access_token']
    print(".......LOGIN REQUEST IS DONE.......")
    print(".......=====================.......\n\n")
    head = {"Authorization": f"Bearer {token1}"}
    return head

def checkorgname():
    organizationName =json_data['organizationName']
    url=base_url+ f"/checkorgname?organizationName={organizationName}"
    res1=requests.get(url, headers=head)
    resp=res1.json()
    # assert resp['data']['result']['isAvailable']=="true" , "The organization name is already exists"
    print(".......CHECK ORG NAME REQUEST IS DONE.......")
    print(".......=====================.......\n\n")
    
    
def domainRequest():
    domaimName =json_data['subDomain']
    url=base_url+ f"/checkdomain?domain={domaimName}"
    res1=requests.get(url, headers=head)
    resp=res1.json()
    # assert resp['data']['result']['isAvailable']=="true" , "The organization name is already exists"
    print(".......CHECK DOMAIN NAME REQUEST IS DONE.......")
    print(".......=====================.......\n\n")

def logoRequest():
    url =base_url+ "/org/logoupload"
    with open("C:/Users/aravi/Desktop/APIautomationPython/1692856405Boat1c.svg", "rb") as svg_file:
        svg_content = svg_file.read()
    res2 = requests.post(url,data=svg_content, headers=head)
    # resp=res2.json()
    # assert resp['status']=="Success", "Logo upload failiure"
    # logopath=resp['data']['result']['logoPath']
    # print(logopath)
    print(".......UPLOAD LOGO REQUEST IS DONE.......")
    print(".......=====================.......\n\n")
    # return logopath
    

# This API use for Adding Organization by giving unique name 
def addOrganization():
    url =base_url+ "/addorganization"
    res2 = requests.post(url, json=json_data, headers=head)
    # assert res2.status_code==200, "Creation Failed "
    resp= res2.json()
    # response= json.dumps(resp ,indent=4)
    global appkey
    appkey=resp['data']['result']['organization']['appKey']
    # print(response)
    print(".......ADD ORGANIZATION  IS DONE.......")
    print(".......=====================.......\n\n")   
    
# This API used for to GET the single Organization data by passing the “appkey”  
def getRequest():
    url=base_url+"/org/" +appkey
    res3=requests.get(url, headers=head)
    assert res3.status_code==200, "Get Request Failed "
    # resp=res3.json()
    # response= (json.dumps(resp , indent=4))
    # print(response)
    print(".......GET REQUEST USING APPKEY IS DONE.......")
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
    


head =post1Request()
checkorgname()
domainRequest()
logoRequest()
addOrganization()
getRequest()
listdb()
