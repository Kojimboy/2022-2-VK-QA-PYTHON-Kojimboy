import uuid

import allure

from ui.locators import basic_locators
from ui.pages.base_page import BasePage


class NewSegmentPage(BasePage):
    locators = basic_locators.NewSegmentPageLocators()
    url = 'https://target-sandbox.my.com/segments/segments_list/new'

    @allure.step("New segment input filling and saving")
    def new_app_game_segment(self):
        self.find(self.locators.APP_GAME_SEGMENT).click()
        self.find(self.locators.APPS_GAMES_CHECKBOX).click()
        self.find(self.locators.ADD_SEGMENT_BUTTON).click()
        segment_name_input = self.find(self.locators.SEGMENT_NAME_INPUT)
        segment_name_input.clear()
        segment_name = str(uuid.uuid1())
        segment_name_input.send_keys(segment_name)
        self.find(self.locators.CREATE_SEGMENT_BUTTON).click()
        return segment_name

    @allure.step("New vk ok segment input filling and saving")
    def new_vk_ok_segment(self, source_name):
        self.find(self.locators.GROUP_VK_OK_SEGMENT).click()
        search_group_input = self.find(self.locators.SEARCH_GROUP_INPUT)
        search_group_input.clear()
        search_group_input.send_keys(source_name)
        self.find(self.locators.CHECKBOX_WITH_SEARCH).click()
        self.find(self.locators.ADD_SEGMENT_BUTTON).click()
        segment_name_input = self.find(self.locators.SEGMENT_NAME_INPUT)
        segment_name_input.clear()
        segment_name = str(uuid.uuid1())
        segment_name_input.send_keys(segment_name)
        self.find(self.locators.CREATE_SEGMENT_BUTTON).click()
        return segment_name
