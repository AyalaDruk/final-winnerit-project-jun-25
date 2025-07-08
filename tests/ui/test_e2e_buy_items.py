import re
from playwright.sync_api import Page, expect

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_e2e_add_to_cart_and_checkout(page: Page,logged_in_user) -> None:
    # Create InventoryPage object (represents the products page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    # Add multiple products to the shopping cart
    inventory_page.add_product_to_cart("sauce-labs-backpack")
    inventory_page.add_product_to_cart("sauce-labs-bike-light")
    inventory_page.add_product_to_cart("sauce-labs-bolt-t-shirt")
    inventory_page.add_product_to_cart("sauce-labs-fleece-jacket")
    # Verify the cart badge shows the correct number of items
    inventory_page.expect_cart_badge_count(4)
    # Navigate to the shopping cart page
    inventory_page.go_to_cart()
    expect(page.url).to_have_url("https://www.saucedemo.com/cart.html")
    # Verify products in cart
    cart_page.expect_product_in_cart("Sauce Labs Backpack")
    cart_page.expect_product_in_cart("Sauce Labs Bike Light")
    cart_page.expect_product_in_cart("Sauce Labs Bolt T-Shirt")
    cart_page.expect_product_in_cart("Sauce Labs Fleece Jacket")
    # Proceed to Checkout
    cart_page.proceed_to_checkout()
    cart_page.verify_cart_subtotal_simple()






def test_example(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    page.locator("[data-test=\"add-to-cart-sauce-labs-bike-light\"]").click()
    page.locator("[data-test=\"add-to-cart-sauce-labs-fleece-jacket\"]").click()
    expect(page.locator("[data-test=\"shopping-cart-badge\"]")).to_contain_text("3")
    # expect(page.locator("[data-test=\"primary-header\"]")).to_match_aria_snapshot("- text: Swag Labs")
    # expect(page.locator("[data-test=\"secondary-header\"]")).to_match_aria_snapshot("- text: Products Name (A to Z)\n- combobox:\n  - option \"Name (A to Z)\" [selected]\n  - option \"Name (Z to A)\"\n  - option \"Price (low to high)\"\n  - option \"Price (high to low)\"")
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    page.locator("[data-test=\"checkout\"]").click()
    page.locator("[data-test=\"firstName\"]").click()
    page.locator("[data-test=\"firstName\"]").fill("abc")
    page.locator("[data-test=\"lastName\"]").click()
    page.locator("[data-test=\"lastName\"]").fill("abc")
    page.locator("[data-test=\"postalCode\"]").click()
    page.locator("[data-test=\"postalCode\"]").fill("201111")
    page.locator("[data-test=\"continue\"]").click()
    page.locator("[data-test=\"finish\"]").click()
    expect(page.locator("[data-test=\"pony-express\"]")).to_be_visible()
    expect(page.locator("[data-test=\"complete-header\"]")).to_contain_text("Thank you for your order!")
    expect(page.locator("[data-test=\"back-to-products\"]")).to_be_visible()
    page.get_by_role("button", name="Open Menu").click()
    page.locator("[data-test=\"logout-sidebar-link\"]").click()