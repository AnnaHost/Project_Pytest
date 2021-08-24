from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPanelLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    REGISTRATION_LINK = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASCET_LINK = (By.CSS_SELECTOR, ".btn-add-to-basket")
