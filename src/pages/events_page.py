import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from src.pages.base_page import BasePage
from src.components.filter_panel import FilterPanel
from src.components.event_card import EventCard
from src.components.header import Header


class EventsPage(BasePage):

    URL = "https://www.greencity.cx.ua/#/greenCity/events"

    def __init__(self, driver):
        super().__init__(driver)
        self.filter_panel = FilterPanel(driver)
        self.event_card = EventCard(driver)
        self.header = Header(driver)

    @allure.step("Open Events page")
    def open(self):
        self.driver.get(self.URL)

    @allure.step("Open event type filter")
    def open_filter(self):
        self.filter_panel.open_type_filter()

    @allure.step("Select 'All types' option")
    def select_all_types(self):
        self.filter_panel.click(self.filter_panel.ALL_TYPES_OPTION)

    @allure.step("Get all filter options")
    def get_options(self):
        return self.filter_panel.get_options()
