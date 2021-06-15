from test_settings import APP_HOST, APP_PORT
from ui.locators.basic_locators import RegistrationPageLocators
from ui.pages.base_page import BasePage


class RegistrationPage(BasePage):
    locators = RegistrationPageLocators()

    def register(self, userdata):
        self.click(self.locators.CREATE_ACC_LINK_LOCATOR)
        self.send_keys(self.locators.USERNAME_INPUT_LOCATOR, userdata['username'])
        self.send_keys(self.locators.PASS_INPUT_LOCATOR, userdata['password'])
        self.send_keys(self.locators.REPEAT_PASS_INPUT_LOCATOR, userdata['pass_repeat'])
        self.send_keys(self.locators.EMAIL_INPUT_LOCATOR, userdata['email'])
        self.click(self.locators.ACCEPT_LOCATOR)
        self.click(self.locators.REGISTER_BUTTON_LOCATOR)

    def register_without_accept(self, userdata):
        self.click(self.locators.CREATE_ACC_LINK_LOCATOR)
        self.send_keys(self.locators.USERNAME_INPUT_LOCATOR, userdata['username'])
        self.send_keys(self.locators.PASS_INPUT_LOCATOR, userdata['password'])
        self.send_keys(self.locators.REPEAT_PASS_INPUT_LOCATOR, userdata['pass_repeat'])
        self.send_keys(self.locators.EMAIL_INPUT_LOCATOR, userdata['email'])
        self.click(self.locators.REGISTER_BUTTON_LOCATOR)

    def is_registration_page(self):
        return self.driver.current_url == f'http://{APP_HOST}:{APP_PORT}/reg'

    def go_to_login(self):
        self.click(self.locators.CREATE_ACC_LINK_LOCATOR)
        self.click(self.locators.GO_TO_LOGIN_LINK_LOCATOR)
        return self.driver
