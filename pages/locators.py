from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPanelLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    REGISTRATION_LINK = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASCET_LINK = (By.CSS_SELECTOR, ".btn-add-to-basket ")

    ALERT_BOOK_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    ALERT_BOOK_NAME = (
        By.CSS_SELECTOR, ".alert-success:first-child .alertinner strong")

    CART_BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    CART_BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
