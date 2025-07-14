import pytest

@pytest.mark.api
def test_update_user(users_api):

   # Verify that updating a user returns the updated data and updatedAt timestamp.

    payload = {
        "name": "morpheus",
        "job": "zion resident"
    }

    response = users_api.put("/users/2", payload)

    users_api.validate_status_code(response, 200)

    response_body = response.json()

    users_api.validate_json_key_values(
        response_body,
        {
            "name": payload["name"],
            "job": payload["job"],
            "updatedAt": None
        }
    )