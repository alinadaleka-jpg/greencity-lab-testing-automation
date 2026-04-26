from selenium.webdriver.common.by import By
from src.components.base_component import BaseComponent


class EventCard(BaseComponent):

    ALL_CARDS = (By.CSS_SELECTOR, "app-event-card")
    CARD_TITLE = (By.CSS_SELECTOR, ".event-title, .title")
    CARD_DATE = (By.CSS_SELECTOR, ".event-date, .date")
    CARD_TYPE_TAG = (By.CSS_SELECTOR, ".event-tag, mat-chip, .tag")
    CARD_IMAGE = (By.CSS_SELECTOR, "img")

    def get_all_cards(self):
        return self.find_all(self.ALL_CARDS)

    def get_card_count(self):
        return len(self.get_all_cards())

    def get_card_title(self, card_element):
        try:
            return card_element.find_element(*self.CARD_TITLE).text.strip()
        except Exception:
            return ""

    def get_card_date(self, card_element):
        try:
            return card_element.find_element(*self.CARD_DATE).text.strip()
        except Exception:
            return ""

    def get_card_tags(self, card_element):
        try:
            tags = card_element.find_elements(*self.CARD_TYPE_TAG)
            return [t.text.strip() for t in tags]
        except Exception:
            return []

    def click_card(self, card_element):
        self.driver.execute_script("arguments[0].click();", card_element)
