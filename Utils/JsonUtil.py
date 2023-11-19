import json

from faker import Faker


class JsonUtil:
    @staticmethod
    def write_json(file_path, json_data):
        with open(file_path, 'w') as file:
            json.dump(json_data, file, indent=4)

    @staticmethod
    def read_json(file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data

    def generate_random_json_data(self, file_path):
        fake = Faker()

        name = fake.name()
        email = fake.email()

        json_data = {
            "name": name,
            "email": email
        }

        self.write_json(file_path, json_data)
