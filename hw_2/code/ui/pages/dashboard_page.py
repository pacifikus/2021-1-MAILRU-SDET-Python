import os

import allure
from selenium.common.exceptions import TimeoutException

from ..locators.basic_locators import DashboardPageLocators
from ..pages.base_page import BasePage
from ..pages.segments_list_page import SegmentListPage


class DashboardPage(BasePage):

    locators = DashboardPageLocators()

    @allure.step('Going to segments list')
    def go_to_segments(self):
        self.click(DashboardPageLocators.SEGMENTS_LINK_LOCATOR)
        return SegmentListPage(self.driver)

    @allure.step('Adding new campaign')
    def add_campaign(self):
        target_url = 'https://postnauka.ru/'
        template = 'test'
        image_path = os.path.join(os.getcwd(), 'img.jpg')
        self.click(self.locators.CREATE_CAMPAIGN_BUTTON_LOCATOR)
        self.click(self.locators.TRAFFIC_TYPE_ITEM_LOCATOR)
        self.send_keys(self.locators.URL_INPUT_LOCATOR, target_url)
        self.click(self.locators.ADV_FORMAT_LOCATOR)
        self.send_keys(self.locators.TITLE_INPUT_LOCATOR, template)
        self.send_keys(self.locators.DESCRIPTION_INPUT_LOCATOR, template)
        self.send_keys(self.locators.UPLOAD_IMAGE_INPUT_LOCATOR, image_path)
        self.click(self.locators.CREATE_CAMPAIGN_SUBMIT_LOCATOR)

    def has_campaigns(self):
        try:
            self.find(self.locators.CAMPAIGNS_TABLE_LOCATOR)
            return True
        except TimeoutException:
            return False

    @allure.step('Removing the added campaign')
    def remove_campaign(self):
        self.click(self.locators.CHECKBOX_CAMPAIGN_LOCATOR)
        self.click(self.locators.CAMPAIGN_CONTROLS_MODULE_LOCATOR)
        self.click(self.locators.REMOVE_CAMPAIGN_LOCATOR)
