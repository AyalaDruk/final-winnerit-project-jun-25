import allure
from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class CheckoutCompletePage(BasePage):
    URL = "https://www.saucedemo.com/checkout-complete.html"

    def __init__(self, page: Page):
        super().__init__(page)
        self.__complete_header = page.locator(".complete-header").describe("Thank You Header")
        self.__back_home_button = page.locator("[data-test='back-to-products']").describe("Back Home Button")
        self.__menu_button = page.locator("#react-burger-menu-btn").describe("Menu Button")
        self.__logout_link = page.locator("#logout_sidebar_link").describe("Logout Link")

    # Verify that the Thank You message is displayed after completing the order.
    def expect_order_complete_message(self):
        with allure.step("Verify purchase completed successfully"):
            expect(self.__complete_header).to_have_text("Thank you for your order!")

    # Click the 'Back Home' button to return to the Inventory page.
    def return_to_inventory(self):
        with allure.step("Click on 'Back Home' button"):
            self.click_element(self.__back_home_button)

    # Open the side menu and click on the Logout link to log out.
    def logout(self):
        with allure.step("Log out of the system"):
            self.click_element(self.__menu_button)
            self.click_element(self.__logout_link)
