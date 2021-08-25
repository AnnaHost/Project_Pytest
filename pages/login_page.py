from .locators import BasePageLocators
from .base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    def should_be_login_url(self):
        print("should_be_login_url is checking\n")
        # реализуйте проверку на корректный url адрес
        assert self.browser.current_url(
            "http://selenium1py.pythonanywhere.com/accounts/login/"), "Текущая страница некорректная"

    def should_be_login_form(self):
        print("should_be_login_form is checking\n")
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(
            *BasePageLocators.LOGIN_LINK), "Отсутствует форма логина"

    def should_be_register_form(self):
        print("should_be_register_form is checking\n")
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(
            *BasePageLocators.REGISTRATION_LINK), "Отсутствует форма регистрации"
