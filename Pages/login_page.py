from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login URL is malformed"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "Login email is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Login password is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login button is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), "Registration email is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD1), "Registration password is not " \
                                                                                   "presented "
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD2), "Registration re-password is not " \
                                                                                   "presented "
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_BUTTON), "Register button is not presented"

    def register_new_user(self, email, password):
        email_link = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email_link.send_keys(email)
        password_link = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1)
        password_link.send_keys(password)
        password_link = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2)
        password_link.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        register_button.click()
