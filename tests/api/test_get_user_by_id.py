import pytest
from assertpy import assert_that


@pytest.mark.api
def test_get_user_by_id(users_api):
    response = users_api.get_user(2)

    # Hard validation: check status code
    users_api.validate_status_code(response, 200)
    response_body = response.json()

    # Validate main JSON keys
    users_api.validate_json_key_values(
        response_body,
        {
            "data": None,
            "support": None
        }
    )

    # Validate user fields and values
    users_api.validate_json_key_values(
        response_body["data"],
        {
            "id": 2,
            "first_name": "Janet",
            "email": "janet.weaver@reqres.in",
            "last_name": None,
            "avatar": None
        }
    )

    # Soft validation: use assertpy for additional checks
    assert_that(response_body["data"]["email"]).contains("@")
