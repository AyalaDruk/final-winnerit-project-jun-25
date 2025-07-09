import re
from playwright.sync_api import Page, expect

from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_e2e_add_to_cart_and_checkout(all_pages, logged_in_user) -> None:
    # Create InventoryPage object (represents the products page)
    inventory_page, cart_page, checkout_page, overview_page, complete_page = all_pages
    # inventory_page = InventoryPage(page)
    #cart_page = CartPage(page)
    # checkout_page = CheckoutPage(page)
    #checkout_complete_page = CheckoutCompletePage(page)
    #checkout_overview_page = CheckoutOverviewPage(page)

    # Add multiple products to the shopping cart
    inventory_page.add_product_to_cart("sauce-labs-backpack")
    inventory_page.add_product_to_cart("sauce-labs-bike-light")
    inventory_page.add_product_to_cart("sauce-labs-bolt-t-shirt")
    inventory_page.add_product_to_cart("sauce-labs-fleece-jacket")

    # Verify the cart badge shows the correct number of items
    inventory_page.expect_cart_badge_count(4)

    # Navigate to the shopping cart page
    inventory_page.go_to_cart()

    # Verify products in cart
    cart_page.expect_product_in_cart("Sauce Labs Backpack")
    cart_page.expect_product_in_cart("Sauce Labs Bike Light")
    cart_page.expect_product_in_cart("Sauce Labs Bolt T-Shirt")
    cart_page.expect_product_in_cart("Sauce Labs Fleece Jacket")

    # Proceed to Checkout
    cart_page.proceed_to_checkout()

    # Fill checkout form
    checkout_page.fill_checkout_information("Ayala", "Druk", "12345")
    checkout_page.proceed_to_overview()

    # Verify order summary and finish
    overview_page.expect_overview_page_loaded()
    overview_page.verify_cart_subtotal_simple()
    overview_page.finish_checkout()

    # Verify Thank You page and logout
    complete_page.expect_order_complete_message()
    complete_page.logout()



