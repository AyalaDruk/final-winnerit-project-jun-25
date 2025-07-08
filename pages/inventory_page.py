from playwright.sync_api import Page, expect
import allure



class InventoryPage:
    def __init__(self, page: Page):
        self.__page = page
        self.__cart_badge = page.locator("[data-test='shopping-cart-badge']").describe("Cart Badge")
        self.__cart_link = page.locator("[data-test='shopping-cart-link']").describe("Cart Link")

    #Add a product to the cart based on its product ID
    def add_product_to_cart(self, product_id: str):
        with allure.step(f"Add product '{product_id}' to the cart"):
         self.__page.locator(f'[data-test="add-to-cart-{product_id}"]').describe(f"Add to Cart Button for {product_id}").click()

   #Navigate to the Cart Page by clicking on the cart link
    def go_to_cart(self):
        with allure.step("Navigate to Cart Page"):
         self.__cart_link.click()

    # Verify that the cart badge shows the expected number of items.
    def expect_cart_badge_count(self, expected_count: int):
        with allure.step(f"Verify cart badge count is '{expected_count}'"):
         expect(self.__cart_badge).to_contain_text(str(expected_count))