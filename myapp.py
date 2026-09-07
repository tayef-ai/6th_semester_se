import requests
import json

# URL = "http://127.0.0.1:8000/student/1/"

# r = requests.get(url=URL)

# data = r.json()

# print(data)

URL = "http://127.0.0.1:8000/createstudent/"

data = {
    'name': 'akon',
    'roll': 12,
    'section': '6DM'
}

json_data = json.dumps(data)

r = requests.post(url=URL, data=json_data)

data = r.json()

print(data)

