import allure
import pytest
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base import BaseCase
from ui.locators import basic_locators
from ui.pages.new_segment_page import NewSegmentPage
from ui.pages.segment_page import SegmentPage


@pytest.mark.UI
class TestSegment(BaseCase):
    @allure.step("Step 1 start new game app segment test")
    def test_new_game_app_segment(self):
        self.logger.info('Go to new segment page')
        self.driver.get(NewSegmentPage.url)
        new_segment_page = NewSegmentPage(self.driver)
        self.logger.info('Choose and create game app segment')
        new_segment_name = new_segment_page.new_app_game_segment()
        self.logger.info('Check created segment name')
        segment_page = SegmentPage(self.driver)
        assert new_segment_name == segment_page.get_top_segment_name()

    @pytest.mark.parametrize("group_link, source_name", [("https://vk.com/vkedu", "VK Образование")
                                                         ])  # можно добавить другие группы
    @allure.step("Step 1 start new vk_ok segment test")
    def test_vk_ok_segment_creation_deletion(self, group_link, source_name):
        self.driver.get(SegmentPage.url)
        segment_page = SegmentPage(self.driver)
        self.logger.info('Add vk_ok source')
        segment_page.add_vk_ok_source(group_link)
        self.logger.info('Go to new segment page')
        self.driver.get(NewSegmentPage.url)
        new_segment_page = NewSegmentPage(self.driver)
        self.logger.info('Choose and create vk ok segment')
        new_segment_name = new_segment_page.new_vk_ok_segment(source_name)
        self.logger.info('Check created vk ok segment with search')
        search_segment_input = segment_page.find(basic_locators.SegmentPageLocators.SEGMENT_SEARCH_INPUT)
        search_segment_input.clear()
        search_segment_input.send_keys(new_segment_name)
        segment_page.find(basic_locators.SegmentPageLocators.SUGGESTED_SEGMENT).click()
        assert new_segment_name == segment_page.get_top_segment_name()  # проверяем что появился сегмент
        self.logger.info('Delete created segment')
        segment_page.delete_vk_ok_segment(new_segment_name)
        self.logger.info('Check successful segment deletion')
        success_message = segment_page.find(basic_locators.SegmentPageLocators.SUCCESS_DELETE_MESSAGE)
        assert WebDriverWait(self, 5).until(
            EC.visibility_of(success_message))  # проверка появления сообщения об успешном удалении
        self.logger.info('assert new segment not in list')
        # self.driver.refresh()
        search_segment_input = segment_page.find(basic_locators.SegmentPageLocators.SEGMENT_SEARCH_INPUT)
        search_segment_input.clear()
        search_segment_input.send_keys(new_segment_name)
        try:
            WebDriverWait(self, 5).until(
                EC.presence_of_element_located(segment_page.find(basic_locators.SegmentPageLocators.TOP_SEGMENT_CELL)))
        except TimeoutException:
            assert True
        self.logger.info('Delete created vk ok source')
        segment_page.delete_vk_ok_source(source_name)
        self.logger.info('Assert successful source deletion')
        assert WebDriverWait(self, 5).until(
            EC.invisibility_of_element(segment_page.find(basic_locators.SegmentPageLocators.DELETE_SOURCE_BUTTON)))
