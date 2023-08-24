import requests
import json

e = {
    "name": "aravind",
    "job": "aravind"
} 
d = {
    "name": "aravind",
    "job": "aravind"
}
    
def getRequest():
    res1 = requests.get("https://reqres.in/api/users/2")
    assert res1.status_code == 200, "Data didn't retrieve successfully"
    response=res1.json()
    resx=json.dumps(response, indent=4)
    print(resx)
    print("*******************************************")
    print("...........get request.....................\n\n")
    
def postRequest():
    res3 = requests.post("https://reqres.in/api/users?page=2", data=e )
    assert res3.status_code == 201, "Data creation failed"
    response=res3.json()
    resx=json.dumps(response, indent=4)
    print(resx)  
    print("*******************************************")
    print("...........post request.....................\n\n")
    
def putRequest():  
    res2 = requests.put("https://reqres.in/api/users/2", data=d)
    assert res2.status_code == 200, "Data update failed"
    response=res2.json()
    resx=json.dumps(response, indent=4)
    print(resx)
    print("*******************************************")
    print("...........put request.....................\n\n")  
    
def deleteRequest():
    res4 = requests.delete("https://reqres.in/api/users/2")
    assert res4.status_code == 204, "Data deletion failed"
    print("*******************************************")
    print("...........delete request.....................")
    
getRequest()
postRequest()
putRequest()
deleteRequest()