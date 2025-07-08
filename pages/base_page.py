# methods have current url
from playwright.sync_api import expect
from playwright.sync_api import Page, expect
import allure
#BasePage: Common utilities for all pages
class BasePage:

    def __init__(self, page: Page):
        self.page = page


    def navigate_to(self, url: str):
       with allure.step(f"Navigate to '{url}'"):
         self.page.goto(url)


    def expect_url(self, expected_url: str):
        with allure.step(f"Verify page URL is '{expected_url}'"):
         self.expect_url(expected_url)


    def click_element(self, locator):
      with allure.step("Click on element"):
        locator.click()


    def fill_text(self, locator, text: str):
        with allure.step(f"Fill text '{text}' in element"):
         locator.fill(text)


