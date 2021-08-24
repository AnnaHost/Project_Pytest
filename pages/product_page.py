from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def add_item_to_basket(self):
        print("search add button..\n")
        add_button = self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASCET_LINK)
        add_button.click()
        print("Button click")

    def check_item_name(self):
        print("check_item_name..\n")
        alert_book_name = self.browser.find_element(
            *ProductPageLocators.ALERT_BOOK_NAME).text
        cart_book_name = self.browser.find_element(
            *ProductPageLocators.CART_BOOK_NAME).text
        assert alert_book_name == cart_book_name, "Названия не совпадают!"
        print(
            f"alert_book_name is {alert_book_name} and cart_book_name is {cart_book_name}\n")

    def check_item_price(self):
        print("check_item_name..\n")
        alert_book_price = self.browser.find_element(
            *ProductPageLocators.ALERT_BOOK_PRICE).text
        cart_book_price = self.browser.find_element(
            *ProductPageLocators.CART_BOOK_PRICE).text
        assert alert_book_price == cart_book_price, "Названия не совпадают!"
        print(
            f"alert_book_name is {alert_book_price} and cart_book_name is {cart_book_price}\n")
