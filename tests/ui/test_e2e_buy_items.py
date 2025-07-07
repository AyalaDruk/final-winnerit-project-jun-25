import re
from playwright.sync_api import Page, expect

def test_end_to_end(page: Page,logged_in_user) -> None:
    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    page.locator("[data-test=\"add-to-cart-sauce-labs-bike-light\"]").click()
    page.locator("[data-test=\"add-to-cart-sauce-labs-bolt-t-shirt\"]").click()
    page.locator("[data-test=\"add-to-cart-sauce-labs-fleece-jacket\"]").click()
    expect(page.locator("[data-test=\"shopping-cart-badge\"]")).to_contain_text("4")
    page.locator("[data-test=\"shopping-cart-link\"]").click()





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