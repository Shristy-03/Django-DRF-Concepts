import requests
import json

# Create operation
URL_C="http://127.0.0.1:8000/stu_create/"

def post_data():    
    data = {
    "name": "Aaryadha",
    "roll": 150,
    "city": "Delhi"
    }
    json_data=json.dumps(data)

    r=requests.post(url=URL_C, data=json_data)

    data=r.json()
    print(data)

# post_data()

# read operation
URL_R="http://127.0.0.1:8000/stu_detail/"

def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    r=requests.get(url=URL_R, data=json_data)
    data=r.json()
    print(data)

# get_data()
# get_data(1)

#update operation
URL_U="http://127.0.0.1:8000/stu_update/"

def put_data():
    data={
        'id':1,
        'roll':105,
        'city':'Jalandhar'
    }

    json_data=json.dumps(data)

    r=requests.put(url=URL_U, data=json_data)

    data=r.json()
    print(data)

# put_data()

# delete operation 
URL_D="http://127.0.0.1:8000/stu_delete/"
def delete_data():
    data={
        'id':1
    }

    json_data=json.dumps(data)

    r=requests.delete(url=URL_D, data=json_data)

    data=r.json()
    print(data)

# delete_data()
