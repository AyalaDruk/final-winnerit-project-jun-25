import pytest


@pytest.mark.ui
@pytest.mark.e2e
@pytest.mark.positive
def test_e2e_remove_item_and_checkout(all_pages, logged_in_user, fill_checkout_and_proceed) -> None:
    # End-to-End test: Add multiple items to cart, remove one, and complete checkout

    # Create InventoryPage object (represents the products page)
    inventory_page, cart_page, checkout_page, overview_page, complete_page = all_pages

    # Add multiple products to cart
    inventory_page.add_items_to_cart([
        "sauce-labs-backpack",
        "sauce-labs-bike-light",
        "sauce-labs-bolt-t-shirt"
    ])

    # Verify cart badge shows correct count
    inventory_page.expect_cart_badge_count(3)

    # Navigate to cart page
    inventory_page.go_to_cart()

    # Verify all products in cart
    cart_page.expect_products_in_cart([
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
        "Sauce Labs Bolt T-Shirt"
    ])

    # Remove one product from cart
    cart_page.remove_product_from_cart("Sauce Labs Bolt T-Shirt")

    # Verify cart badge updated
    inventory_page.expect_cart_badge_count(2)

    # Proceed to checkout
    cart_page.proceed_to_checkout()

    # Use fixture to fill and proceed
    fill_checkout_and_proceed("Ayala", "Druk", "12345")

    # Complete order and logout
    # Finish checkout
    overview_page.verify_cart_totals()
    overview_page.finish_checkout()

    # Verify Thank You page and logout
    complete_page.expect_order_complete_message()
    complete_page.logout()
