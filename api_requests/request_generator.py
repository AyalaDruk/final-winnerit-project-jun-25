import requests
from requests import Response
from dotenv import load_dotenv
import os

load_dotenv()


class RequestGenerator:
    def __init__(self, base_url: str):
        self.__base_url = base_url
        self.__headers = {"x-api-key": os.getenv("X_API_KEY")}

    def get(self, endpoint: str):
        return requests.get(f"{self.__base_url}{endpoint}", headers=self.__headers)

    def post(self, endpoint: str, data: dict):
        return requests.post(f"{self.__base_url}{endpoint}", json=data, headers=self.__headers)

    def put(self, endpoint: str, data: dict) -> Response:
        return requests.put(f"{self.__base_url}{endpoint}", json=data, headers=self.__headers)

    def delete(self, endpoint: str) -> Response:
        return requests.delete(f"{self.__base_url}{endpoint}", headers=self.__headers)

    def validate_status_code(self, response: Response, expected_status_code: int):
        assert response.status_code == expected_status_code

    # Check that all expected keys exist in the JSON response.
    def validate_json_key_values(self, json_obj: dict, expected_data: dict):
        for key, expected_value in expected_data.items():
            assert key in json_obj
            if expected_value is not None:
                actual_value = json_obj[key]
                assert actual_value == expected_value
