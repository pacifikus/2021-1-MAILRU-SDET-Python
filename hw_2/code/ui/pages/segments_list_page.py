import allure
from selenium.common.exceptions import TimeoutException

from ..locators.basic_locators import SegmentsPageLocators
from ..pages.base_page import BasePage


class SegmentListPage(BasePage):
    locators = SegmentsPageLocators()

    @allure.step('Adding new segment')
    def add_segment(self, segment_name):
        self.click(self.locators.NEW_SEGMENT_LINK_LOCATOR)
        self.click(self.locators.SEGMENT_SOURCE_CHECKBOX_LOCATOR)
        self.click(self.locators.ADD_SEGMENT_BUTTON_LOCATOR)
        title = self.find(self.locators.TITLE_SEGMENT_INPUT_LOCATOR)
        title.click()
        title.send_keys(segment_name)
        self.click(self.locators.CREATE_SEGMENT_BUTTON_LOCATOR)

    @allure.step('Removing the added segment')
    def remove_segment(self):
        self.click(self.locators.REMOVE_SEGMENT_ICON_LOCATOR)
        self.click(self.locators.REMOVE_SEGMENT_CONFIRM_BUTTON_LOCATOR)

    def has_segments(self):
        try:
            self.find(self.locators.NEW_SEGMENT_LINK_LOCATOR)
            return False
        except TimeoutException:
            return True
