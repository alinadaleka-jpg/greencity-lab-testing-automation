from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from src.components.base_component import BaseComponent


class FilterPanel(BaseComponent):

    TIME_FILTER = (By.XPATH,
        "(//div[contains(@class,'filter-list')]//mat-select)[1]")
    LOCATION_FILTER = (By.XPATH,
        "(//div[contains(@class,'filter-list')]//mat-select)[2]")
    STATUS_FILTER = (By.XPATH,
        "(//div[contains(@class,'filter-list')]//mat-select)[3]")
    TYPE_FILTER = (By.XPATH,
        "(//div[contains(@class,'filter-list')]//mat-select)[4]")

    ALL_TYPES_OPTION = (By.XPATH,
        "//mat-option[.//span[contains(text(),'Всі типи')]]")
    ALL_OPTIONS = (By.TAG_NAME, "mat-option")

    ACTIVE_CHIPS = (By.CSS_SELECTOR, ".mat-mdc-chip, mat-chip")

    CLEAR_BUTTON = (By.XPATH, "//span[contains(text(),'Очистити')]")

    def open_type_filter(self):
        self.click(self.TYPE_FILTER)
        self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "div.cdk-overlay-pane")
            )
        )

    def select_all_types(self):
        self.open_type_filter()
        self.click(self.ALL_TYPES_OPTION)

    def get_options(self):
        return self.find_all(self.ALL_OPTIONS)

    def get_active_chips(self):
        return self.driver.find_elements(*self.ACTIVE_CHIPS)

    def clear_filters(self):
        self.click(self.CLEAR_BUTTON)

    def open_time_filter(self):
        self.click(self.TIME_FILTER)
        self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "div.cdk-overlay-pane")
            )
        )
