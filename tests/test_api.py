import teapot
from teapot import json

from . import TestBase, responses

users = [
    {
        "id": 1,
        "first_name": "John",
        "last_name": "Doe"
    },
    {
        "id": 2,
        "first_name": "Jane",
        "last_name": "Doe"
    }
]

new_user = {
    "id": 3,
    "first_name": "New",
    "last_name": "New"
}


class Users:
    @responses.activate
    def create(self, user):
        responses.add("POST", "/users",
                      body=json.dumps(user), status=201,
                      content_type="application/json")
        resp = self.client.post("http://localhost/users")
        return resp.json()

    @responses.activate
    def add(self, user):
        body = {"op": "add"}
        body.update(user)
        responses.add("PATCH", "/users",
                      body=json.dumps(user), status=201,
                      content_type="application/json")
        resp = self.client.patch("http://localhost/users")
        return resp.json()

    @responses.activate
    def delete(self, user_id):
        responses.add("DELETE", "/users/{}".format(user_id),
                      status=204, content_type="application/json")
        return self.client.delete(
            "http://localhost/users/{}".format(user_id))

    @responses.activate
    def get(self, user_id):
        responses.add("GET", "/users/{}".format(user_id),
                      body=json.dumps(users[user_id - 1]), status=200,
                      content_type="application/json")
        url = "http://localhost/users/{}".format(user_id)
        resp = self.client.get(url)
        return resp.json()

    @responses.activate
    def head(self, user_id):
        responses.add("HEAD", "/users/{}".format(user_id),
                      status=200, content_type="application/json")
        url = "http://localhost/users/{}".format(user_id)
        return self.client.head(url)

    @responses.activate
    def get_all(self):
        responses.add("GET", "/users",
                      body=json.dumps(users), status=200,
                      content_type="application/json")
        resp = self.client.get("http://localhost/users")
        return resp.json()

    @responses.activate
    def invalid(self):
        responses.add("GET", "/invalid", status=400,
                      content_type="application/json")
        resp = self.client.get("http://localhost/invalid")
        return resp.json()

    @responses.activate
    def options(self):
        responses.add("OPTIONS", "/", status=200,
                      adding_headers={"Allow": "GET"})
        return self.client.options("http://localhost/")

    @responses.activate
    def change_first_name(self, user_id, first_name):
        u = users[user_id - 1]
        u['first_name'] = first_name
        responses.add("PUT", "/users/{}".format(user_id),
                      body=json.dumps(u), status=200,
                      content_type="application/json")
        url = "http://localhost/users/{}".format(user_id)
        resp = self.client.put(url)
        return resp.json()


class MyTestResource:
    pass


class TestAPI(TestBase):
    def setUp(self):
        self.base_setup()
        self.resource = MyTestResource()

    def test_adding_resource(self):
        self.api.add_resource(self.resource)
        assert self.api._resources["MyTestResource"] == self.api.MyTestResource
        assert self.api.__getattr__("MyTestResource") == self.api.MyTestResource

        self.api.add_resource(self.resource, "MyResourceName")
        assert self.api._resources["MyResourceName"] == self.api.MyResourceName
        assert self.api.__getattr__("MyResourceName") == self.api.MyResourceName

    def test_custom_attributes(self):
        self.api.add_resource(self.resource)
        assert self.api._attrs["custom_attr"] == "foobar"
        assert self.api.MyTestResource.custom_attr == "foobar"

    def test_users_resource_methods(self):
        self.api.add_resource(Users())
        assert self.api._resources["Users"] == self.api.Users
        assert self.api.__getattr__("Users") == self.api.Users

        delete = self.api.Users.delete(1)
        options = self.api.Users.options()
        change = self.api.Users.change_first_name(1, "Jim")
        head = self.api.Users.head(1)

        assert self.api.Users.get_all() == users
        assert self.api.Users.get(1) == users[0]
        assert self.api.Users.create(new_user) == new_user
        assert self.api.Users.add(new_user) == new_user
        assert change["first_name"] == "Jim"
        assert delete.status == 204
        assert options.getheader("Allow") == "GET"
        assert head.status == 200
        self.assertRaises(
            teapot.exceptions.HTTPResponseError, self.api.Users.invalid)

    def test_adding_existing_resource(self):
        self.api.add_resource(Users())
        self.assertRaises(NameError, self.api.add_resource, Users())
