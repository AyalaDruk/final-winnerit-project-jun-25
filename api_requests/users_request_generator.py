import allure

from api_requests.request_generator import RequestGenerator


class UsersRequestGenerator(RequestGenerator):
    def __init__(self, base_url: str = "https://reqres.in/api"):
        super().__init__(base_url)

    def get_user(self, user_id: int):
      with allure.step(f"Fetch user with ID: {user_id}"):
        return self.get(f"/users/{user_id}")

    def create_user(self, data: dict):
     with allure.step(f"Create new user with data: {data}"):
        return self.post("/users", data)

    # Fetch a list of users for the given page.
    def list_users(self, page: int = 1):
      with allure.step(f"Fetch list of users on page: {page}"):
        return self.get(f"/users?page={page}")