import allure
from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class CheckoutOverviewPage(BasePage):
    URL = "https://www.saucedemo.com/checkout-step-two.html"

    def __init__(self, page: Page):
        super().__init__(page)
        self.__overview_header = self.page.locator(".title").describe("Checkout Overview Header")
        self.__finish_button = self.page.locator("[data-test='finish']").describe("Finish Button")
        self.__item_prices = self.page.locator(".inventory_item_price").describe("Item Prices")
        self.__summary_subtotal = self.page.locator(".summary_subtotal_label").describe("Summary Subtotal")

    # Verify that the Checkout Overview page is displayed by checking the header text
    def expect_overview_page_loaded(self):
        with allure.step("Verify that the Checkout Overview page is loaded"):
            expect(self.__overview_header).to_have_text("Checkout: Overview")

        # Verify that subtotal matches the sum of all item prices

    def verify_cart_subtotal_simple(self):
        with allure.step("Verify that subtotal matches the sum of all item prices"):
            # Get all prices as text
            prices_text = self.__item_prices.all_text_contents()
            # Convert prices to float and calculate total
            total_from_items = sum([float(price[1:]) for price in prices_text])
            # Get the displayed subtotal
            subtotal_text = self.__summary_subtotal.inner_text(timeout=5000)
            subtotal_displayed = float(subtotal_text.split("$")[1])
            # Compare calculated total with displayed subtotal
            assert total_from_items == subtotal_displayed, \
                f" Subtotal mismatch! Calculated: ${total_from_items}, Displayed: ${subtotal_displayed}"
            print(f" Subtotal verified successfully: ${total_from_items}")

    # Click the 'Finish' button to complete the checkout process.
    def finish_checkout(self):
        with  allure.step("Click on 'Finish' button to complete the order"):
            self.click_element(self.__finish_button)
