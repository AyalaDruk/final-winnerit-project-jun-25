import pytest
from assertpy import assert_that


@pytest.mark.api
def test_get_users_with_delay(users_api):
    # Verify GET /users?delay=3 returns a valid response after delay.

    response = users_api.get("/users?delay=3")

    users_api.validate_status_code(response, 200)
    response_body = response.json()

    # Validate main JSON keys
    users_api.validate_json_key_values(
        response_body,
        {
            "page": None,
            "per_page": None,
            "total": None,
            "total_pages": None,
            "data": None,
            "support": None
        }
    )

    assert_that(response_body["data"]).is_type_of(list).is_not_empty()
