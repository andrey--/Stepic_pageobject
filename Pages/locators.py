from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form")
    LOGIN_EMAIL = (By.CSS_SELECTOR, "input#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "input#id_login-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary[name='login_submit']")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "form#register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "input#id_registration-email")
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "input#id_registration-password1")
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "input#id_registration-password1")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary[name='registration_submit']")


class ProductPageLocators:
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div#messages div.alert.alert-safe.alert-success")
    NAME = (By.CSS_SELECTOR, 'div.col-sm-6.product_main h1')
    ADDED_TO_BASKET = (By.XPATH, '//div[@class="alertinner " and strong/following-sibling::text()]')
    BASKET_TOTAL = (By.XPATH, "//p[contains(text(),'Your basket total is now')]")
    PRICE = (By.CSS_SELECTOR, "div.col-sm-6.product_main p.price_color")
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
