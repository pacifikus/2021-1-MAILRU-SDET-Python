from selenium.webdriver import ActionChains

from ui.locators.basic_locators import AccountPageLocators
from ui.pages.base_page import BasePage


class AccountPage(BasePage):
    locators = AccountPageLocators()

    def go_to_api(self):
        self.click(self.locators.GO_TO_API_LINK_LOCATOR)
        return self.driver

    def go_to_internet(self):
        self.click(self.locators.GO_TO_INTERNET_LINK_LOCATOR)
        return self.driver

    def go_to_smtp(self):
        self.click(self.locators.GO_TO_SMTP_LINK_LOCATOR)
        return self.driver

    def go_to_home(self):
        self.click(self.locators.HOME_LINK_LOCATOR)
        return self.driver

    def go_to_python(self):
        self.click(self.locators.PYTHON_LINK_LOCATOR)
        return self.driver

    def go_to_python_history(self):
        main_item = self.find(self.locators.PYTHON_LINK_LOCATOR)
        sub_item = self.find(self.locators.PYTHON_HISTORY_LINK_LOCATOR)
        ActionChains(self.driver).move_to_element(main_item).click(sub_item).perform()

    def go_to_flask(self):
        main_item = self.find(self.locators.PYTHON_LINK_LOCATOR)
        sub_item = self.find(self.locators.FLASK_LINK_LOCATOR)
        ActionChains(self.driver).move_to_element(main_item).click(sub_item).perform()

    def go_to_centos(self):
        main_item = self.find(self.locators.LINUX_LINK_LOCATOR)
        sub_item = self.find(self.locators.CENTOS_LINK_LOCATOR)
        ActionChains(self.driver).move_to_element(main_item).click(sub_item).perform()

    def go_to_news(self):
        main_item = self.find(self.locators.NETWORK_LINK_LOCATOR)
        sub_item = self.find(self.locators.NEWS_LINK_LOCATOR)
        ActionChains(self.driver).move_to_element(main_item).click(sub_item).perform()

    def go_to_download(self):
        main_item = self.find(self.locators.NETWORK_LINK_LOCATOR)
        sub_item = self.find(self.locators.DOWNLOAD_LINK_LOCATOR)
        ActionChains(self.driver).move_to_element(main_item).click(sub_item).perform()

    def go_to_examples(self):
        main_item = self.find(self.locators.NETWORK_LINK_LOCATOR)
        sub_item = self.find(self.locators.EXAMPLES_LINK_LOCATOR)
        ActionChains(self.driver).move_to_element(main_item).click(sub_item).perform()

    def logout(self):
        self.click(self.locators.LOGOUT_LINK_LOCATOR)
        return self.driver
