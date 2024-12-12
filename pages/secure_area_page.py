from selenium.webdriver.common.by import By

class SecureAreaPage:
    SUCCESS_MESSAGE = (By.ID, "flash")
    HEADING = (By.CSS_SELECTOR, "h2")

    def __init__(self, driver):
        self.driver = driver

    def get_success_message(self):
        return self.driver.find_element(*self.SUCCESS_MESSAGE).text

    def get_heading(self):
        return self.driver.find_element(*self.HEADING).text
