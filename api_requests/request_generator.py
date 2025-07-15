import allure
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
     with allure.step(f"Send GET request to endpoint: {endpoint}"):
        return requests.get(f"{self.__base_url}{endpoint}", headers=self.__headers)

    def post(self, endpoint: str, data: dict):
        with allure.step(f"Send POST request to endpoint: {endpoint} with data: {data}"):
         return requests.post(f"{self.__base_url}{endpoint}", json=data, headers=self.__headers)

    def put(self, endpoint: str, data: dict) -> Response:
        with allure.step(f"Send PUT request to endpoint: {endpoint} with data: {data}"):
         return requests.put(f"{self.__base_url}{endpoint}", json=data, headers=self.__headers)

    def delete(self, endpoint: str) -> Response:
        with allure.step(f"Send DELETE request to endpoint: {endpoint}"):
         return requests.delete(f"{self.__base_url}{endpoint}", headers=self.__headers)

    def patch(self, endpoint: str, data: dict) -> Response:
        with allure.step(f"Send PATCH request to endpoint: {endpoint} with data: {data}"):
         return requests.patch(f"{self.__base_url}{endpoint}", json=data, headers=self.__headers)

    def validate_status_code(self, response: Response, expected_status_code: int):
        with allure.step(f"Validate that status code is {expected_status_code}"):
         assert response.status_code == expected_status_code

    # Check that all expected keys exist in the JSON response.
    def validate_json_key_values(self, json_obj: dict, expected_data: dict):
      with allure.step("Validate JSON keys and values"):
        for key, expected_value in expected_data.items():
            assert key in json_obj
            if expected_value is not None:
                actual_value = json_obj[key]
                assert actual_value == expected_value

    # Validate that the response body is empty.
    def validate_empty_response(self, response: Response):
        with allure.step("Validate that response body is empty"):
         assert response.text == ""
