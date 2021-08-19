import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


link = "https://education-in-russia.com"


def test_show_PS(browser):
    browser.get(link)
