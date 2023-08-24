import requests
import random
import json
import string

#base url:
base_url = "https://gorest.co.in"

#Passing auth token 
auth_token = "Bearer e4b8e1f593dc4a731a153c5ec8cc9b8bbb583ae964ce650a741113091b4e2ac6"

#passing the authorization token as dictionary 
headers = {"Authorization": auth_token}

#generation of random emails
def generate_random_email(length= 6):
    domain = "automation.com"
    random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
    email = random_string + "@" + domain
    return email


def get_request():
    url = base_url + "/public/v2/users"
    print("get url: " + url)
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json GET response body: ", json_str)
    print(".......GET USER IS DONE.......")
    print(".......=====================.......")


def post_request():
    url = base_url + "/public/v2/users"
    print("post url: " + url)
    data = {
        "name": "Naveen Automation",
        "email": generate_random_email(),
        "gender": "male",
        "status": "active"
    }
    response = requests.post(url, json=data, headers=headers)
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json POST response body: ", json_str)
    user_id = json_data["id"]
    print("user id ===>", user_id)
    assert response.status_code == 201
    assert "name" in json_data
    assert json_data["name"] == "Naveen Automation"
    print(".......POST/Create USER IS DONE.......")
    print(".......=====================.......")
    return user_id


def put_request(user_id):
    url = base_url + f"/public/v2/users/{user_id}"
    print("PUT url: " + url)
    data = {
        "name": "Naveen Automation Labs",
        "email": generate_random_email(),
        "gender": "male",
        "status": "inactive"
    }
    response = requests.put(url, json=data, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json PUT response body: ", json_str)
    assert json_data["id"] == user_id
    assert json_data["name"] == "Naveen Automation Labs"
    print(".......PUT/Update USER IS DONE.......")
    print(".......=====================.......")


def delete_request(user_id):
    url = base_url + f"/public/v2/users/{user_id}"
    print("DELETE url: " + url)
    response = requests.delete(url, headers=headers)
    assert response.status_code == 204
    print(".......DELETE USER IS DONE.......")
    print(".......=====================.......")


get_request()
user_id = post_request()
put_request(user_id)
delete_request(user_id)