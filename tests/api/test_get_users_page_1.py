import pytest
from assertpy import assert_that


@pytest.mark.api
def test_get_users_page_1(users_api):
    # Send GET request to fetch all users on page 1
    response = users_api.list_users(page=1)
    # Hard validation: check HTTP status code
    users_api.validate_status_code(response, 200)
    response_body = response.json()
    # Validate that main JSON keys exist
    users_api.validate_json_key_values(
        response_body,
        {"page": None, "per_page": None, "total": None, "data": None}
    )
    # Soft validation: check 'data' is a non-empty list
    assert_that(response_body["data"]).is_type_of(list).is_not_empty()
    # Validate keys for the first user in the list
    users_api.validate_json_key_values(
        response_body["data"][0],
        {"id": 1, "first_name": "George", "email": "george.bluth@reqres.in"}
    )
    # Assert the total number of users matches 'per_page'
    assert_that(len(response_body["data"])).is_equal_to(response_body["per_page"])
