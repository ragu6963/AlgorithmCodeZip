import requests

url = "http://httpbin.org/"
headers = {"Content-Type": "application/json; charset=utf-8"}


def get(params):
    uri = ""
    uri = url + uri
    response = requests.get(uri, params=params, headers={"X-Auth-Token": token})
    status = response.status_code
    json = response.json()
    return json


def post(json):
    uri = "response-headers"
    uri = url + uri
    response = requests.post(uri, json=json)
    # response = requests.post(uri, json=json, headers={"X-Auth-Token": token})
    json = response.json()
    return json


def patch():
    uri = ""
    uri = url + uri
    response = requests.patch(uri)
    json = response.json()
    return json


def put():
    uri = ""
    uri = url + uri
    response = requests.put(uri)
    json = response.json()
    return json


def delete():
    uri = ""
    uri = url + uri
    response = requests.delete(uri)
    json = response.json()
    return json


def solve():
    # print(get("get"))
    print(post({"freeform": 2222}))


if __name__ == "__main__":
    solve()
