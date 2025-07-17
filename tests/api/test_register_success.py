import pytest


@pytest.mark.api
def test_register_success(users_api):
    # Verify successful registration returns id and token.

    payload = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }

    # Send POST request to register
    response = users_api.post("/register", payload)

    users_api.validate_status_code(response, 200)

    response_body = response.json()

    # Validate response keys
    users_api.validate_json_key_values(
        response_body,
        {
            "id": 4,
            "token": "QpwL5tke4Pnpja7X4"
        }
    )
