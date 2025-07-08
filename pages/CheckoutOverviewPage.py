import allure
from playwright.sync_api import Page, expect


class CheckoutOverviewPage:

    def __init__(self, page: Page):
        self.__page = page
        self.__overview_header = page.locator(".title").describe("Checkout Overview Header")
        self.__finish_button = page.locator("[data-test='finish']").describe("Finish Button")

    #Verify that the Checkout Overview page is displayed by checking the header text
    def expect_overview_page_loaded(self):
        with allure.step("Verify that the Checkout Overview page is loaded"):
         expect(self.__overview_header).to_have_text("Checkout: Overview")

    # Click the 'Finish' button to complete the checkout process.
    def finish_checkout(self):
        allure.step("Click on 'Finish' button to complete the order")
        self.__finish_button.click()

