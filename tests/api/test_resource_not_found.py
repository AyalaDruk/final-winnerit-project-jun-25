import pytest


@pytest.mark.api
def test_patch_user(users_api):
   # Verify that patching a user returns updated data and updatedAt timestamp.

    payload = {
        "job":  "zion resident"
    }

    response = users_api.patch("/users/2", payload)

    users_api.validate_status_code(response, 200)

    response_body = response.json()

    users_api.validate_json_key_values(
        response_body,
        {
            "job": payload["job"],
            "updatedAt": None
        }
    )