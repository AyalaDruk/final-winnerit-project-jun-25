import pytest
from  playwright.sync_api import Page
from pages.login_page import LoginPage


@pytest.fixture
def login_page(page: Page):
    return LoginPage(page)

@pytest.fixture
def login_page_with_login(page: Page):
    lp = LoginPage(page)
    lp.navigate()
    lp.expect_login_credentials_visible()
    return lp

@pytest.fixture
def logged_in_user(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.expect_login_credentials_visible()
    login_page.type_username("standard_user")
    login_page.fill_password("secret_sauce")
    login_page.click_login_button()
    login_page.expect_url_to_be("https://www.saucedemo.com/inventory.html")
    return login_page