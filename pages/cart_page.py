from playwright.sync_api import Page, expect


class CartPage:
    def __init__(self, page: Page):
        self.__page = page
        self.__cart_items = page.locator(".cart_item")
        self.__checkout_button = page.locator("[data-test='checkout']")
        self.__item_price = page.locator(".inventory_item_price")
        self.__sub_total=page.locator(".summary_subtotal_label")


    def expect_product_in_cart(self, product_name: str):
        expect(self.__cart_items).to_contain_text(product_name)

    def proceed_to_checkout(self):
        self.__checkout_button.click()

    def verify_cart_subtotal_simple(self):
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


