import pytest
import allure
from selenium.webdriver.common.by import By
from src.pages.events_page import EventsPage


@allure.feature("Events Page")
class TestEventsPage:

    @allure.story("Filter menu opens correctly")
    @allure.title("TC1 - Event type filter menu opens")
    def test_open_event_type_filter_menu(self, driver):
        page = EventsPage(driver)
        page.open()
        page.open_filter()

        options = page.get_options()
        assert len(options) > 0, "Список фільтра не відкрився"

    @allure.story("Default filter state")
    @allure.title("TC2 - Economic filter is not selected by default")
    def test_negative_filter(self, driver):
        page = EventsPage(driver)
        page.open()

        chips = driver.find_elements(
            By.XPATH,
            "//span[contains(text(),'Економічний')]"
        )
        assert len(chips) == 0, "Фільтр не має бути вибраний за замовчуванням"

    @allure.story("Select all event types")
    @allure.title("TC3 - Selecting 'All types' shows all options")
    def test_select_all_event_types(self, driver):
        page = EventsPage(driver)
        page.open()
        page.open_filter()
        page.select_all_types()

        options = page.get_options()
        assert len(options) > 0, "Опції не завантажились"

        option_texts = [opt.text.strip() for opt in options]
        assert "Всі типи" in option_texts, "Опція 'Всі типи' не знайдена"
        assert len(options) >= 4, f"Очікувалось 4+ опції, отримано: {len(options)}"
