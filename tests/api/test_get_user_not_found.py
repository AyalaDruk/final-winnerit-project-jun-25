import pytest
from assertpy import assert_that


@pytest.mark.api
def test_get_user_not_found(users_api):
    # Verify that the API returns 404 for a non-existent user.
    # Send GET request for a user that does not exist
    response = users_api.get_user(999)

    # Hard validation: check status code is 404
    users_api.validate_status_code(response, 404)
    response_body = response.json()

    # Soft validation: check response body is empty or has no 'data' key
    assert_that(response_body).does_not_contain_key("data")
