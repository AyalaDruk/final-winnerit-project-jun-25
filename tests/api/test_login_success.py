import pytest


@pytest.mark.api
def test_login_success(users_api):
    # Verify successful login returns token.

    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    response = users_api.post("/login", payload)

    users_api.validate_status_code(response, 200)

    response_body = response.json()

    users_api.validate_json_key_values(
        response_body,
        {
            "token": "QpwL5tke4Pnpja7X4"
        }
    )
