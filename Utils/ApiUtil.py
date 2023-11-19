import json
import requests


class ApiUtil:
    access_token = None

    def __init__(self, base_url):
        self.base_url = base_url

    @classmethod
    def set_access_token(cls, token):
        cls.access_token = token

    @classmethod
    def get_access_token(cls):
        return cls.access_token

    def login(self, url, username, password):
        response = requests.post(url, data={"username": username, "password": password})
        if response.status_code == 200:
            token = response.json().get("access_token")
            self.set_access_token(token)

    @staticmethod
    def authenticated_post_request(url, data=None):
        headers = {"Authorization": f"Bearer {ApiUtil.get_access_token()}"}
        response = requests.post(url, json=data, headers=headers)
        return response

    def get_request(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url)
        return response

    def post_request(self, endpoint, data=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url, json=data)
        return response

    def post_request_from_json_file(self, endpoint, json_file_path):
        url = f"{self.base_url}/{endpoint}"

        with open(json_file_path, 'r') as file:
            data = json.load(file)

        response = requests.post(url, json=data)
        return response

    def put_request(self, endpoint, data=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.put(url, json=data)
        return response

    def delete_request(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        response = requests.delete(url)
        return response
