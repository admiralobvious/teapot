# teapot

A very thin wrapper around urllib3 in development.

Using the `HTTPAPI`:

```python
import teapot
from teapot import json  # convenience import that will use `python-rapidjson` if it's installed.


class ReqRes:
    # self.client is an instance of `HTTPClient` that gets added automatically to your class
    def login(self):
        return self.client.post("/login", body=json.dumps(self.credentials))

    def get_users(self):
        return self.client.get("/users")

    def get_user(self, user_id):
        return self.client.get(f"/users/{user_id}")

    def create_user(self, data):
        return self.client.post("/users", body=data)

headers = {
    "Content-Type": "application/json",
}

credentials = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}  # gets automatically added as an attribute on `ReqRes`

api = teapot.HTTPAPI(base_url="https://reqres.in/api", headers=headers, credentials=credentials)
api.add_resource(ReqRes())

login = api.ReqRes.login()
print(login.data)  # returns the raw bytes
# b'{"token":"QpwL5tke4Pnpja7X4"}'
print(login.json())
# {'token': 'QpwL5tke4Pnpja7X4'}

users = api.ReqRes.get_users()
print(users.json())
# {'page': 1, 'per_page': 3, 'total': 12, 'total_pages': 4, 'data': [{'id': 1, 'email': 'george.bluth@reqres.in', 'first_name': 'George', 'last_name': 'Bluth', 'avatar': 'https://s3.amazonaws.com/uifaces/faces/twitter/calebogden/128.jpg'}, {'id': 2, 'email': 'janet.weaver@reqres.in', 'first_name': 'Janet', 'last_name': 'Weaver', 'avatar': 'https://s3.amazonaws.com/uifaces/faces/twitter/josephstein/128.jpg'}, {'id': 3, 'email': 'emma.wong@reqres.in', 'first_name': 'Emma', 'last_name': 'Wong', 'avatar': 'https://s3.amazonaws.com/uifaces/faces/twitter/olegpogodaev/128.jpg'}]}

user = api.ReqRes.get_user(2)
print(user.json())
# {'data': {'id': 2, 'email': 'janet.weaver@reqres.in', 'first_name': 'Janet', 'last_name': 'Weaver', 'avatar': 'https://s3.amazonaws.com/uifaces/faces/twitter/josephstein/128.jpg'}}

user = {
    "name": "morpheus",
    "job": "leader"
}

create = api.ReqRes.create_user(json.dumps(user))
print(create.json())
# {'name': 'morpheus', 'job': 'leader', 'id': '929', 'createdAt': '2019-05-29T21:21:31.491Z'}

```

Using the `HTTPClient`:

```python
import teapot
from teapot import json


headers = {
    "Content-Type": "application/json",
}

credentials = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}

client = teapot.HTTPClient(base_url="https://reqres.in/api", headers=headers)

login = client.post("/login", body=json.dumps(credentials))
# you can also use the .request() method and pass the HTTP methods yourself
# login = client.request("POST", "/login", body=json.dumps(credentials))
print(login.data)  # returns the raw bytes
# b'{"token":"QpwL5tke4Pnpja7X4"}'

print(login.json())
# {'token': 'QpwL5tke4Pnpja7X4'}

users = client.get("/users")
print(users.json())
# {'page': 1, 'per_page': 3, 'total': 12, 'total_pages': 4, 'data': [{'id': 1, 'email': 'george.bluth@reqres.in', 'first_name': 'George', 'last_name': 'Bluth', 'avatar': 'https://s3.amazonaws.com/uifaces/faces/twitter/calebogden/128.jpg'}, {'id': 2, 'email': 'janet.weaver@reqres.in', 'first_name': 'Janet', 'last_name': 'Weaver', 'avatar': 'https://s3.amazonaws.com/uifaces/faces/twitter/josephstein/128.jpg'}, {'id': 3, 'email': 'emma.wong@reqres.in', 'first_name': 'Emma', 'last_name': 'Wong', 'avatar': 'https://s3.amazonaws.com/uifaces/faces/twitter/olegpogodaev/128.jpg'}]}

user = client.get("/users/2")
print(user.json())
# {'data': {'id': 2, 'email': 'janet.weaver@reqres.in', 'first_name': 'Janet', 'last_name': 'Weaver', 'avatar': 'https://s3.amazonaws.com/uifaces/faces/twitter/josephstein/128.jpg'}}

user = {
    "name": "morpheus",
    "job": "leader"
}

create = client.post("/users", body=json.dumps(user))
print(create.json())
# {'name': 'morpheus', 'job': 'leader', 'id': '929', 'createdAt': '2019-05-29T21:21:31.491Z'}
```
