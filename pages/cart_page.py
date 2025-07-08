import allure
from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class CartPage(BasePage):
    URL = "https://www.saucedemo.com/cart.html"

    def __init__(self, page: Page):
        super().__init__(page)
        self.__cart_items = self._page.locator(".cart_item").describe("Cart Items List")
        self.__checkout_button = self._page.locator("[data-test='checkout']").describe("Checkout Button")
        self.__item_price = self._page.locator(".inventory_item_price").describe("Item Price")
        self.__sub_total = self._page.locator(".summary_subtotal_label").describe("Subtotal Label")

    # Verify that a specific product is present in the cart
    def expect_product_in_cart(self, product_name: str):
        with allure.step(f"Verify that product '{product_name}' exists in the cart"):
            expect(self.__cart_items).to_contain_text(product_name)

    # Click the Checkout button to proceed to the checkout flow.
    def proceed_to_checkout(self):
        with allure.step("Click on 'Checkout' button"):
            self.click_element(self.__checkout_button)

    # Check if the sum of all individual item prices matches the subtotal displayed on the cart page.
    def verify_cart_subtotal_simple(self):
        with allure.step("Verify that subtotal matches the sum of all item prices"):
            # Get all prices as text
            prices_text = self.__item_price.all_text_contents()
            # Convert prices to float and calculate total
            total_from_items = sum([float(price[1:]) for price in prices_text])
            # Get the displayed subtotal
            subtotal_text = self.__sub_total.text_content()
            subtotal_displayed = float(subtotal_text.split("$")[1])
            # Compare calculated total with displayed subtotal
            assert total_from_items == subtotal_displayed, \
                f" Subtotal mismatch! Calculated: ${total_from_items:.2f}, Displayed: ${subtotal_displayed}"
            print(f" Subtotal verified successfully: ${total_from_items}")
