from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form")
    LOGIN_EMAIL = (By.CSS_SELECTOR, "input#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "input#id_login-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary[name='login_submit']")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "form#register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "input#id_registration-email")
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "input#id_registration-password1")
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "input#id_registration-password1")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary[name='registration_submit']")
