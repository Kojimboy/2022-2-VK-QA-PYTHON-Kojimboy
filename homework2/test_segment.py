import allure
import pytest

from base import BaseCase
from ui.locators import basic_locators
from ui.pages.new_segment_page import NewSegmentPage
from ui.pages.segment_page import SegmentPage


@pytest.mark.UI
class TestSegment(BaseCase):
    @allure.step("Go to new segment page")
    def test_game_app_segment(self):
        self.driver.get(NewSegmentPage.url)
        new_segment_page = NewSegmentPage(self.driver)
        new_segment_name = new_segment_page.new_app_game_segment()
        self.logger.info('Check created segment name')
        segment_page = SegmentPage(self.driver)
        assert new_segment_name == segment_page.get_top_segment_name()

    @pytest.mark.parametrize("group_link, source_name", [("https://vk.com/vkedu", "VK Образование")
                                                         ])  # можно добавить другие группы
    @allure.step("Go to segment list page")
    def test_vk_ok_segment(self, group_link, source_name):
        self.driver.get(SegmentPage.url)
        segment_page = SegmentPage(self.driver)
        segment_page.add_vk_ok_source(group_link)
        self.logger.info('Go to new segment page')
        self.driver.get(NewSegmentPage.url)
        new_segment_page = NewSegmentPage(self.driver)
        new_segment_name = new_segment_page.new_vk_ok_segment(source_name)
        self.logger.info('Check created vk ok segment with search')
        search_segment_input = segment_page.find(basic_locators.SegmentPageLocators.SEGMENT_SEARCH_INPUT)
        search_segment_input.clear()
        search_segment_input.send_keys(new_segment_name)
        segment_page.find(basic_locators.SegmentPageLocators.SUGGESTED_SEGMENT).click()
        assert new_segment_name == segment_page.get_top_segment_name()  # проверяем что появился сегмент
        segment_page.delete_vk_ok_segment(new_segment_name)
        segment_page.delete_vk_ok_source(source_name)
