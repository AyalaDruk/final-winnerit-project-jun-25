from playwright.sync_api import Page, expect
from pages.base_page import BasePage
import allure


class InventoryPage(BasePage):
    inventory_url = "https://www.saucedemo.com/inventory.html"

    def __init__(self, page: Page):
        super().__init__(page)
        self.__cart_badge = self.page.locator("[data-test='shopping-cart-badge']").describe("Cart Badge")
        self.__cart_link = self.page.locator("[data-test='shopping-cart-link']").describe("Cart Link")


        # Add multiple products to the cart
    def add_items_to_cart(self, product_ids: list[str]):
        with allure.step(f"Add products to the cart: {product_ids}"):
            for product_id in product_ids:
                product_locator = self.page.locator(f'[data-test="add-to-cart-{product_id}"]')
                self.click_element(product_locator)

    # Navigate to the Cart Page by clicking on the cart link
    def go_to_cart(self):
        with allure.step("Navigate to Cart Page"):
            self.click_element(self.__cart_link)

    # Verify that the cart badge shows the expected number of items.
    def expect_cart_badge_count(self, expected_count: int):
        with allure.step(f"Verify cart badge count is '{expected_count}'"):
            expect(self.__cart_badge).to_contain_text(str(expected_count))
