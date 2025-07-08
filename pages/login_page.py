from playwright.sync_api import Page, expect
from pages.base_page import BasePage
import allure


class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"

    def __init__(self, page: Page):
        super().__init__(page)
        self.__username_field = self._page.locator("#user-name").describe("Username Field")
        self.__password_field = self._page.locator('[name="password"]').describe("Password Field")
        self.__login_button = self._page.locator("[data-test=login-button]")
        self._error_massage = self._page.locator("[data-test=\"error\"]").describe("Login Error Message")
        self.__login_credentials = self._page.locator("[data-test=\"login-credentials\"]").describe(
            "Login Credentials Section")

    # # Methods
    def click_login_button(self):
        self.click_element(self.__login_button)

    def fill_password(self, password: str):
        self.fill_text(self.__password_field, password)

    def navigate(self):
        with  allure.step("Navigate to Login Page"):
            self.navigate_to(self.URL)

    def type_username(self, username: str):
        with allure.step(f"Typing '{username}' into username field"):
            self.__username_field.press_sequentially(username, delay=100)

    # # Assertions

    def expect_error_message(self, expected_text: str):
        with allure.step(f"Expecting error message to contain: '{expected_text}'"):
            expect(self._error_massage).to_contain_text(expected_text)

    def expect_login_credentials_visible(self):
        with allure.step("Expecting login credentials section to be visible"):
            expect(self.__login_credentials).to_be_visible()

    def expect_url_to_be(self, expected_url: str):
        self.expect_url(expected_url)
