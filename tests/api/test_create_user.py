import pytest
from assertpy import assert_that

@pytest.mark.api
def test_create_user(users_api):

   # Verify that a new user can be created via POST /users.

    # Payload for creating user
    payload = {
        "name": "morpheus",
        "job": "leader"
    }

    response = users_api.create_user(payload)

    users_api.validate_status_code(response, 201)

    response_body = response.json()

    users_api.validate_json_key_values(
        response_body,
        {
            "name": "morpheus",
            "job": "leader",
            "id": None,
            "createdAt": None
        }
    )

    # soft assertions
    assert_that(response_body["name"]).is_equal_to(payload["name"])
    assert_that(response_body["job"]).is_equal_to(payload["job"])
    assert_that(response_body["id"]).is_not_empty()
    assert_that(response_body["createdAt"]).is_not_empty()