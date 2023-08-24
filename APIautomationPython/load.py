import random
import string
import json

b1= {
    "user_name" : "admin",
    "password": "Admin@123"
}
b2={
    "firstName": "super1",
    "lastName": "admin1",
    "userName":"admin1",
    "email":"admin1@123",
    "password": "Admin1@123"
}

def generate_random_name(length=5):
    random_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
    return random_name
def generate_random_email(length=5):
    random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
    email = random_string + "@mailinator.com"
    return email
name=generate_random_name()
name1=generate_random_name()
email= generate_random_email()

b3 = {
    "organizationName": name,
    "subDomain": name1,
    "companyCategory": "IT",
    "logoPath": "https://hrms-poc.s3.eu-west-1.amazonaws.com/test-company2.svg",
    "active": True,
    "orgAddress": "dfdfsdf",
    "orgPincode": "34545",
    "orgCountry": 9,
    "orgState": None,
    "orgCity": None,
    "primary": {
        "firstName": "ram",
        "lastName": "kumar",
        "phone": "+91333543245",
        "designation": "CEO",
        "role": 1,
        "email": email,
        "address": "123 Main Street",
        "country": 9,
        "state": None,
        "city": None,
        "pincode": "dsdsd",
        "isPrimary": 1
    },
    "packages": [
        1
    ]
}
b31 =json.dumps(b3 ,indent=4)
print(b31)
