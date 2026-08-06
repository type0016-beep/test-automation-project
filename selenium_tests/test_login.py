import pytest
from selenium.webdriver.common.by import By
from selenium_tests.locators.login_locators import LoginPageLocators

def test_successful_login(browser):
    browser.get("https://www.saucedemo.com/")
    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()
    assert "inventory" in browser.current_url