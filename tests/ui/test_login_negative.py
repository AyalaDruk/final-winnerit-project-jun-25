import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


@pytest.mark.ui
@pytest.mark.negative
def test_login_locked_out_user(page:Page,login_page)->None:
  login_page.navigate()
  login_page.expect_login_credentials_visible()
  login_page.type_username("locked_out_user")
  login_page.fill_password("secret_sauce")
  login_page.click_login_button()
  login_page.expect_error_message("Epic sadface: Sorry, this user has been locked out.")

@pytest.mark.ui
@pytest.mark.negative
def test_login_invalid_username(page:Page,login_page_with_login)->None:
  login_page_with_login.type_username("ascxcf")
  login_page_with_login.fill_password("secret_sauce")
  login_page_with_login.click_login_button()
  login_page_with_login.expect_error_message("Epic sadface: Username and password do not match any user in this service")

@pytest.mark.ui
@pytest.mark.negative
@pytest.mark.parametrize("username,password,error_message", [
    ("", "secret_sauce", "Epic sadface: Username is required"),
    ("standard_user", "", "Epic sadface: Password is required"),
])
def test_login_empty_username_and_password(page: Page, username, password, error_message,login_page):
    login_page.navigate()
    login_page.expect_login_credentials_visible()
    login_page.type_username(username)
    login_page.fill_password(password)
    login_page.click_login_button()
    login_page.expect_error_message(error_message)

