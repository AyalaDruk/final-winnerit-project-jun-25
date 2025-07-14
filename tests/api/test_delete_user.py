import pytest


@pytest.mark.api
def test_delete_user(users_api):
    # Verify that deleting an existing user returns 204 No Content.

    response = users_api.delete("/users/2")

    users_api.validate_status_code(response, 204)

    # Validate response body is empty
    users_api.validate_empty_response(response)


