import pytest
from assertpy import assert_that


@pytest.mark.api
def test_get_users_page_2(users_api):
    # Verify that the API returns users for page 2.

    # Send GET request for page 2
    response = users_api.list_users(page=2)

    # Validate status code
    users_api.validate_status_code(response, 200)

    # Parse JSON response
    response_body = response.json()

    # Validate JSON keys
    users_api.validate_json_key_values(
        response_body,
        {
            "page": None,
            "per_page": None,
            "total": None,
            "total_pages": None,
            "data": None
        }
    )

    # Validate page number
    assert_that(response_body["page"]).is_equal_to(2)

    # Validate 'data' is a non-empty list
    assert_that(response_body["data"]).is_type_of(list).is_not_empty()
