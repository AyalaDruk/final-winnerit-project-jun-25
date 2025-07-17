import pytest
from assertpy import assert_that


@pytest.mark.api
def test_get_resource_list(users_api):
    # Verify GET /unknown returns a list of resources with expected keys.

    response = users_api.get("/unknown")

    users_api.validate_status_code(response, 200)

    response_body = response.json()

    assert_that(response_body["data"]).is_type_of(list).is_not_empty()

    users_api.validate_json_key_values(
        response_body,
        {
            "page": 1,
            "per_page": 6,
            "total": 12,
            "total_pages": 2,
        }
    )

    first_resource = response_body["data"][0]
    users_api.validate_json_key_values(
        first_resource,
        {
            "id": 1,
            "name": "cerulean",
            "year": 2000,
            "color": "#98B2D1",
            "pantone_value": "15-4020"
        }
    )

    # Validate  with assertpy
    support_data = response_body["support"]
    assert_that(support_data).contains_key("url", "text")
