import pytest


@pytest.mark.api
def test_delete_user_not_found(users_api):
   # Verify that deleting a non-existent user still returns 204 No Content (reqres mock API).

    response = users_api.delete("/users/999")
    users_api.validate_status_code(response, 204)

    # Validate response body is empty
    users_api.validate_empty_response(response)
