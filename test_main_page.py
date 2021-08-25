import py
import pytest
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
import time


@pytest.mark.loguin_guest
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.basket
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.basket_should_be_empty()
    page.chec_item_in_basket()
