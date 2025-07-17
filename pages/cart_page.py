import allure
from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class CartPage(BasePage):
    URL = "https://www.saucedemo.com/cart.html"

    def __init__(self, page: Page):
        super().__init__(page)
        self.__cart_items = self.page.locator(".cart_item").describe("Cart Items List")
        self.__checkout_button = self.page.locator("[data-test='checkout']").describe("Checkout Button")

    # Verify that a specific product is present in the cart

    def expect_products_in_cart(self, product_names: list[str]):
        with allure.step(f"Verify products in cart: {product_names}"):
            for product_name in product_names:
                product_locator = self.page.locator(f".cart_item:has-text('{product_name}')")
                expect(product_locator).to_be_visible()

        # Remove a specific product from the cart

    def remove_product_from_cart(self, product_name: str):
        with allure.step(f"Remove product '{product_name}' from the cart"):
            # Locate the product block by its name
            product_block = self.page.locator(f".cart_item:has-text('{product_name}')")
            # Find the remove button inside the block
            remove_button = product_block.locator("button.cart_button")
            # Click using BasePage method
            self.click_element(remove_button)

    # Click the Checkout button to proceed to the checkout flow.
    def proceed_to_checkout(self):
        with allure.step("Click on 'Checkout' button"):
            self.click_element(self.__checkout_button)
