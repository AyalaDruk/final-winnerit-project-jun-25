import pytest
from playwright.sync_api import Page, expect

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

@pytest.mark.ui
@pytest.mark.positive
def test_login_standard_user_success( login_page: LoginPage) -> None:
    login_page.navigate()
    login_page.type_username("standard_user")
    login_page.fill_password("secret_sauce")
    login_page.click_login_button()
    login_page.expect_url_to_be(InventoryPage.inventory_url)

@pytest.mark.ui
@pytest.mark.positive
def test_login_problem_user_success( login_page: LoginPage) -> None:
    login_page.navigate()
    login_page.expect_login_credentials_visible()
    login_page.type_username("problem_user")
    login_page.fill_password("secret_sauce")
    login_page.click_login_button()
    login_page.expect_url_to_be(InventoryPage.inventory_url)

@pytest.mark.ui
@pytest.mark.positive
def test_login_performance_glitch_user_success(page: Page, login_page: LoginPage) -> None:
    login_page.navigate()
    login_page.expect_login_credentials_visible()
    login_page.type_username("performance_glitch_user")
    login_page.fill_password("secret_sauce")
    login_page.click_login_button()
    login_page.expect_url_to_be(InventoryPage.inventory_url)

@pytest.mark.ui
@pytest.mark.positive
def test_login_visual_user_success(page: Page, login_page: LoginPage) -> None:
    login_page.navigate()
    login_page.expect_login_credentials_visible()
    login_page.type_username("visual_user")
    login_page.fill_password("secret_sauce")
    login_page.click_login_button()
    login_page.expect_url_to_be(InventoryPage.inventory_url)
