import allure
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from ui.locators import basic_locators
from ui.pages.base_page import BasePage


class SegmentPage(BasePage):
    locators = basic_locators.SegmentPageLocators()
    url = 'https://target-sandbox.my.com/segments/segments_list'

    @allure.step("Get created segment name")
    def get_top_segment_name(self):
        self.driver.get(SegmentPage.url)
        new_segment_cell = self.find(self.locators.TOP_SEGMENT_CELL)
        return new_segment_cell.get_attribute("title")

    @allure.step("Add desired vk_ok source")
    def add_vk_ok_source(self, source):
        self.driver.get(SegmentPage.url)
        self.find(self.locators.VK_OK_GROUP_DATA_SOURCE_BUTTON).click()
        source_name_input = self.find(self.locators.VK_OK_GROUP_NAME_INPUT)
        source_name_input.clear()
        source_name_input.send_keys(source)
        self.find(self.locators.SHOW_GROUP_BUTTON).click()
        self.find(self.locators.VK_EDU_GROUP).click()
        self.find(self.locators.ADD_SELECTED_GROUP_BUTTON).click()

    @allure.step("Delete created vk_ok source with assertion")
    def delete_vk_ok_source(self, source):
        self.driver.get(SegmentPage.url)
        self.find(self.locators.VK_OK_GROUP_DATA_SOURCE_BUTTON).click()
        search_input = self.find(self.locators.SOURCE_SEARCH_INPUT)
        search_input.clear()
        search_input.send_keys(source)
        self.find(self.locators.SUGGESTED_SOURCE).click()
        self.find(self.locators.DELETE_SOURCE_BUTTON).click()
        self.find(self.locators.CONFIRM_DELETE_SOURCE_BUTTON).click()
        assert WebDriverWait(self, 5).until(
            EC.invisibility_of_element(self.find(basic_locators.SegmentPageLocators.DELETE_SOURCE_BUTTON)))

    @allure.step("Delete created vk_ok segment with assertion")
    def delete_vk_ok_segment(self, segment_name):
        self.driver.get(SegmentPage.url)
        search_segment_input = self.find(basic_locators.SegmentPageLocators.SEGMENT_SEARCH_INPUT)
        search_segment_input.clear()
        search_segment_input.send_keys(segment_name)
        self.find(basic_locators.SegmentPageLocators.SUGGESTED_SEGMENT).click()
        self.find(self.locators.TOP_SEGMENT_CHECKBOX).click()
        self.find(self.locators.ACTION_BUTTON).click()
        self.find(self.locators.DELETE_SEGMENT_BUTTON).click()
        success_message = self.find(basic_locators.SegmentPageLocators.SUCCESS_DELETE_MESSAGE)
        assert WebDriverWait(self, 5).until(
            EC.visibility_of(success_message))  # проверка появления сообщения об успешном удалении
        search_segment_input = self.find(basic_locators.SegmentPageLocators.SEGMENT_SEARCH_INPUT)
        search_segment_input.clear()
        search_segment_input.send_keys(segment_name)
        try:
            WebDriverWait(self, 5).until(
                EC.presence_of_element_located(self.find(basic_locators.SegmentPageLocators.TOP_SEGMENT_CELL)))
        except TimeoutException:
            assert True
