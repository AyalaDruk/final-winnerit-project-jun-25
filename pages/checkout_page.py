import allure
from playwright.sync_api import Page


class CheckoutPage:
    """
    This class represents the Checkout Information page where the user fills out shipping details.
    """

    def __init__(self, page: Page):
        self.__page = page
        self.__first_name_field = page.locator("[data-test='firstName']").describe("First Name Field")
        self.__last_name_field = page.locator("[data-test='lastName']").describe("Last Name Field")
        self.__postal_code_field = page.locator("[data-test='postalCode']").describe("Postal Code Field")
        self.__continue_button = page.locator("[data-test='continue']").describe("Continue Button")

    #Fill in the First Name, Last Name, and Postal Code fields on the Checkout page.
    def fill_checkout_information(self, first_name: str, last_name: str, postal_code: str):
        with allure.step(f"Fill checkout information: {first_name} {last_name}, Postal Code: {postal_code}"):
         self.__first_name_field.fill(first_name)
         self.__last_name_field.fill(last_name)
         self.__postal_code_field.fill(postal_code)

#Click the 'Continue' button to proceed to the Checkout Overview page.
    def proceed_to_overview(self):
        with allure.step("Proceed to Checkout Overview page"):
         self.__continue_button.click()