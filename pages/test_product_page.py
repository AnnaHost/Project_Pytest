from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def add_item_to_basket(self):
        print("search add button")
        add_link = self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASCET_LINK)
