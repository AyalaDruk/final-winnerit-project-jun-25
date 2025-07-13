from api_requests.request_generator import RequestGenerator


class UsersRequestGenerator(RequestGenerator):
    def __init__(self, base_url: str = "https://reqres.in/api"):
        super().__init__(base_url)

    def get_user(self, user_id: int):
        return self.get(f"/users/{user_id}")

    def create_user(self, data: dict):
        return self.post("/users", data)

    # Fetch a list of users for the given page.
    def list_users(self, page: int = 1):
        return self.get(f"/users?page={page}")