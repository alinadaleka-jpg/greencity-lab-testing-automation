from selenium.webdriver.common.by import By
from src.components.base_component import BaseComponent


class Header(BaseComponent):

    LOGO = (By.CSS_SELECTOR, "app-header .header-logo")
    NAV_EVENTS = (By.XPATH, "//nav//a[contains(text(),'Події')]")
    NAV_ECO_NEWS = (By.XPATH, "//nav//a[contains(text(),'Еко Новини')]")
    NAV_MAP = (By.XPATH, "//nav//a[contains(text(),'Карта')]")
    NAV_ABOUT = (By.XPATH, "//nav//a[contains(text(),'Про Нас')]")
    SIGN_IN_BUTTON = (By.XPATH, "//a[contains(text(),'Увійти') or contains(text(),'Sign in')]")
    REGISTER_BUTTON = (By.XPATH, "//a[contains(text(),'Зареєструватися')]")
    LANGUAGE_SWITCHER = (By.CSS_SELECTOR, "app-language-switcher")

    def click_events(self):
        self.click(self.NAV_EVENTS)

    def click_eco_news(self):
        self.click(self.NAV_ECO_NEWS)

    def click_map(self):
        self.click(self.NAV_MAP)

    def is_register_button_visible(self):
        try:
            return self.find(self.REGISTER_BUTTON).is_displayed()
        except Exception:
            return False

    def get_current_language(self):
        return self.find(self.LANGUAGE_SWITCHER).text.strip()
