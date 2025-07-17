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
        self.__summary_tax = self.page.locator(".summary_tax_label").describe("Summary Tax")
        self.__summary_total = self.page.locator(".summary_total_label").describe("Summary Total")

    # Verify that the Checkout Overview page is displayed by checking the header text
    def expect_overview_page_loaded(self):
        with allure.step("Verify that the Checkout Overview page is loaded"):
            expect(self.__overview_header).to_have_text("Checkout: Overview")

    # Verify that subtotal matches the sum of all item prices
    def verify_cart_totals(self):
        with allure.step("Verify that total matches item prices + tax"):
            # Get all item prices
            prices_text = self.__item_prices.all_text_contents()
            item_sum = sum([float(price[1:]) for price in prices_text])  # Sum item prices

            # Get displayed tax
            tax_text = self.__summary_tax.inner_text(timeout=5000)
            tax_displayed = float(tax_text.split("$")[1])

            # Get displayed total
            total_text = self.__summary_total.inner_text(timeout=5000)
            total_displayed = float(total_text.split("$")[1])

            # Calculate expected total
            expected_total = item_sum + tax_displayed

            # Assertion
            assert round(expected_total, 2) == round(total_displayed, 2), \
                f"Total mismatch! Expected: ${expected_total}, Displayed: ${total_displayed}"
            print(f"🛒 Displayed Total: ${total_displayed}\n")

    # Click the 'Finish' button to complete the checkout process.
    def finish_checkout(self):
        with  allure.step("Click on 'Finish' button to complete the order"):
            self.click_element(self.__finish_button)
