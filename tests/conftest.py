import pytest
from  playwright.sync_api import Page

from pages.cart_page import CartPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

import allure

class DummyStep:
    def __init__(self, *args, **kwargs):
        pass
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

allure.step = DummyStep


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

@pytest.fixture
def all_pages(page: Page):
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)
    checkout_overview_page = CheckoutOverviewPage(page)
    checkout_complete_page = CheckoutCompletePage(page)
    return (
        inventory_page,
        cart_page,
        checkout_page,
        checkout_overview_page,
        checkout_complete_page
    )