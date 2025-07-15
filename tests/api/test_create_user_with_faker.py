import pytest
from assertpy import assert_that
from faker import Faker

fake = Faker()


@pytest.mark.api
def test_create_user_with_faker(users_api):
    #   Verify POST /users creates a user with random data and returns id and createdAt.

    # Generate random name and job using Faker
    payload = {
        "name": fake.name(),
        "job": fake.job()
    }

    response = users_api.create_user(payload)

    users_api.validate_status_code(response, 201)

    response_body = response.json()

    users_api.validate_json_key_values(
        response_body,
        {
            "name": payload["name"],
            "job": payload["job"],
            "id": None,
            "createdAt": None
        }
    )
    assert_that(response_body["id"]).is_not_empty()
    assert_that(response_body["createdAt"]).is_not_empty()
