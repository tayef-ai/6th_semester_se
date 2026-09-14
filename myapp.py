import requests
import json

# URL = "http://127.0.0.1:8000/student/1/"

# r = requests.get(url=URL)

# data = r.json()

# print(data)

# URL = "http://127.0.0.1:8000/createstudent/"

# data = {
#     'name': 'akon',
#     'roll': 12,
#     'section': '6DM'
# }

# json_data = json.dumps(data)

# r = requests.post(url=URL, data=json_data)

# data = r.json()

# print(data)

# URL = "http://127.0.0.1:8000/createstudent/"

# data = {
#     'id': 5,
#     'name': 'ckon', 
#     'roll': 123,
#     'section': '12DM'
# }

# json_data = json.dumps(data)

# r = requests.put(url=URL, data=json_data)

# res_data = r.json()

# print(res_data)

# URL = "http://127.0.0.1:8000/createstudent/"

# data = {
#     'id': 5,
#     'name': 'ckon', 
#     'section': '19DM'
# }

# json_data = json.dumps(data)

# r = requests.patch(url=URL, data=json_data)

# res_data = r.json()

# print(res_data)

URL = "http://127.0.0.1:8000/createstudent/"

data = {
    'id': 4
}

json_data = json.dumps(data)

r = requests.delete(url=URL, data=json_data)

res_data = r.json()

print(res_data)