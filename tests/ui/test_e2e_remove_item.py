import re
from playwright.sync_api import Page, expect

from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_e2e_remove_item_and_checkout(page: Page, logged_in_user) -> None:
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)
    checkout_overview_page = CheckoutOverviewPage(page)
    checkout_complete_page = CheckoutCompletePage(page)

    # Add multiple products to cart
    inventory_page.add_product_to_cart("sauce-labs-backpack")
    inventory_page.add_product_to_cart("sauce-labs-bike-light")
    inventory_page.add_product_to_cart("sauce-labs-bolt-t-shirt")

    # Verify cart badge shows correct count
    inventory_page.expect_cart_badge_count(3)

    # Navigate to cart page
    inventory_page.go_to_cart()

    # Verify products in cart
    cart_page.expect_product_in_cart("Sauce Labs Backpack")
    cart_page.expect_product_in_cart("Sauce Labs Bike Light")
    cart_page.expect_product_in_cart("Sauce Labs Bolt T-Shirt")

    # Remove one product from cart
    cart_page.remove_product_from_cart("Sauce Labs Bolt T-Shirt")

    # Verify cart badge updated
    inventory_page.expect_cart_badge_count(2)

    # Proceed to checkout
    cart_page.proceed_to_checkout()

    # Fill checkout information
    checkout_page.fill_checkout_information("Ayala", "Druk", "12345")
    checkout_page.proceed_to_overview()

    # Verify overview page loaded and subtotal
    checkout_overview_page.expect_overview_page_loaded()
    checkout_overview_page.verify_cart_subtotal_simple()

    # Finish checkout
    checkout_overview_page.finish_checkout()

    # Verify Thank You page and logout
    checkout_complete_page.expect_order_complete_message()
    checkout_complete_page.logout()
