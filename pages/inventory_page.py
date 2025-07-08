from playwright.sync_api import Page, expect
import allure



class InventoryPage:
    def __init__(self, page: Page):
        self.__page = page
        self.__cart_badge = page.locator("[data-test='shopping-cart-badge']")
        self.__cart_link = page.locator("[data-test='shopping-cart-link']")

    def add_product_to_cart(self, product_id: str):
        self.__page.locator(f'[data-test="add-to-cart-{product_id}"]').click()


    def go_to_cart(self):
        self.__cart_link.click()

    def expect_cart_badge_count(self, expected_count: int):
       expect(self.__cart_badge).to_contain_text(str(expected_count))