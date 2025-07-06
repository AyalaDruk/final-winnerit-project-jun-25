from playwright.sync_api import Page, expect
from pages.login_page import LoginPage



def test_login_negative1(page:Page,login_page)->None:
  login_page.navigate()
  login_page.expect_login_credentials_visible()
  login_page.type_username("locked_out_user")
  login_page.fill_password("secret_sauce")
  login_page.click_login_button()
  login_page.expect_error_message("Epic sadface: Sorry, this user has been locked out.")

def test_login_negative2(page:Page,login_page_with_login)->None:
  login_page_with_login.type_username("ascxcf")
  login_page_with_login.fill_password("secret_sauce")
  login_page_with_login.click_login_button()
  login_page_with_login.expect_error_message("Epic sadface: Username and password do not match any user in this service")

