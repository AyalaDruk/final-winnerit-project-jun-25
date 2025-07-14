import pytest


@pytest.mark.api
def test_login_failure_missing_password(users_api):
    # Verify login fails when password is missing.

    payload = {
        "email": "peter@klaven"
    }

    response = users_api.post("/login", payload)

    users_api.validate_status_code(response, 400)

    response_body = response.json()

    users_api.validate_json_key_values(
        response_body,
        {"error": "Missing password"}
    )
