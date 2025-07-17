import pytest

import pytest


@pytest.mark.api
def test_update_user_not_found(users_api):
    # Update non-existent user returns 200 (reqres mock API)

    payload = {
        "name": "morpheus",
        "job": "zion resident"
    }

    response = users_api.put("/users/999", payload)

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
