import pytest


@pytest.mark.ui
@pytest.mark.e2e
@pytest.mark.positive
def test_e2e_add_to_cart_and_checkout(all_pages, logged_in_user, fill_checkout_and_proceed) -> None:
    #  End-to-End test: Add multiple items to the cart and complete checkout.

    # Create InventoryPage object (represents the products page)
    inventory_page, cart_page, checkout_page, overview_page, complete_page = all_pages

    # Add multiple products to the shopping cart
    inventory_page.add_items_to_cart([
        "sauce-labs-backpack",
        "sauce-labs-bike-light",
        "sauce-labs-bolt-t-shirt",
        "sauce-labs-fleece-jacket"
    ])

    # Verify the cart badge shows the correct number of items
    inventory_page.expect_cart_badge_count(4)

    # Navigate to the shopping cart page
    inventory_page.go_to_cart()

    # Verify all products in cart
    cart_page.expect_products_in_cart([
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Fleece Jacket"
    ])

    # Proceed to Checkout
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
