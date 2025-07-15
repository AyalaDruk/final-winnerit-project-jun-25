import pytest
from playwright.sync_api import Page
from utils.allure_utils import attach_screenshot, attach_video
from api_requests.users_request_generator import UsersRequestGenerator
from pages.cart_page import CartPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
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


@pytest.fixture
def fill_checkout_and_proceed(all_pages):
    # Fixture that fills the checkout form and navigates to the overview page.

    _, _, checkout_page, overview_page, _ = all_pages  # Unpack only needed pages

    def fill(first_name: str, last_name: str, zip_code: str):
        checkout_page.fill_checkout_information(first_name, last_name, zip_code)
        checkout_page.proceed_to_overview()
        overview_page.expect_overview_page_loaded()

    return fill


@pytest.fixture
def users_api():
    # Fixture to initialize UsersRequestGenerator for API tests.
    return UsersRequestGenerator()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    #  Attach screenshot and video to Allure report for **all tests**
    # (pass & fail).

    outcome = yield
    result = outcome.get_result()

    if result.when == "call":
        page = item.funcargs.get("page", None)
        if page:
            attach_screenshot(page, name=f"Screenshot - {item.name}")
            attach_video(page, name=f"Video - {item.name}")
