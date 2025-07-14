import pytest
from assertpy import assert_that


@pytest.mark.api
def test_get_single_resource(users_api):
    # Verify GET /unknown/2 returns a single resource with expected keys and values.

    response = users_api.get("/unknown/2")

    users_api.validate_status_code(response, 200)

    response_body = response.json()

    users_api.validate_json_key_values(
        response_body,
        {
            "data": {
                "id": 2,
                "name": "fuchsia rose",
                "year": 2001,
                "color": "#C74375",
                "pantone_value": "17-2031"
            }
        }
    )
    #Validate  with assertpy
    support_data = response_body["support"]
    assert_that(support_data).contains_key("url", "text")

