from .pages.login_page import LoginPage
from .pages.main_page import MainPage
import time


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    link2 = "http://selenium1py.pythonanywhere.com/pl/accounts/login/"
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    # page = MainPage(browser, link)
    # page.open()                      # открываем страницу
    # # выполняем метод страницы — переходим на страницу логина
    # page.should_be_login_link()
    # page.go_to_login_page()
    page2 = LoginPage(browser, link2)
    page2.open()
    print("1231")
    page2.should_be_login_page()
