from selenium.webdriver.common.by import By

class LoginPageLocators:
    USERNAME = (By.CSS_SELECTOR, "#user-name")
    PASSWORD = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login-button")
    LOGIN_LOGO = (By.CSS_SELECTOR, ".login_logo")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

class InventoryPageLocators:
    PAGE_TITLE = (By.CSS_SELECTOR, ".title")
    ITEM_NAME = (By.CSS_SELECTOR, ".inventory_item_name")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, ".btn_inventory")
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")
    SORT_CONTAINER = (By.CSS_SELECTOR, ".product_sort_container")

class CartPageLocators:
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, ".checkout_button")
    CONTINUE_SHOPPING = (By.CSS_SELECTOR, "#continue-shopping")