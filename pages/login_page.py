from playwright.sync_api import Page, expect
import allure

class LoginPage:
   def __init__(self,page:Page):
       self.__page=page
       self.__username_filed=page.locator("#user-name").describe("Username Field")
       self.__password_filed=page.locator('[name="password"]').describe("Password Field")
       self.__login_button=page.locator("[data-test=login-button]")
       self._error_massage=page.locator("[data-test=\"error\"]").describe("Login Error Message")
       self.__login_credentials = page.locator("[data-test=\"login-credentials\"]").describe("Login Credentials Section")

   # # Methods
   def click_login_button(self):
       self.__login_button.click()

   def fill_password(self,password:str):
       self.__password_filed.fill(password)

   def navigate(self,url="https://www.saucedemo.com/"):
       self.__page.goto(url)

   def type_username(self,username:str):
       self.__username_filed.press_sequentially(username , delay=100)

   # # Assertions

   def expect_error_message(self,expected_text:str):
       expect(self._error_massage).to_contain_text(expected_text)

   def expect_login_credentials_visible(self):
       expect(self.__login_credentials).to_be_visible()




