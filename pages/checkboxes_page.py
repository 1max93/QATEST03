from selenium.webdriver.common.by import By

class CheckboxesPage:
    URL = "https://the-internet.herokuapp.com/checkboxes"
    CHECKBOXES = (By.CSS_SELECTOR, "#checkboxes input")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def get_checkboxes(self):
        return self.driver.find_elements(*self.CHECKBOXES)

    def check_first_box_if_not_checked(self):
        boxes = self.get_checkboxes()
        if not boxes[0].is_selected():
            boxes[0].click()
        return boxes[0].is_selected()
