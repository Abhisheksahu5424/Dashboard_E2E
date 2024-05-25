from datetime import datetime

from selenium.webdriver.common.by import By


class CalenderHandling:
    def __init__(self, driver):
        self.driver = driver

    # driver.find_element(By.CLASS_NAME, "p-button").click()
    Clicking_Calender = (By.CLASS_NAME, "p-button")

    def calender(self):
        return self.driver.find_element(*CalenderHandling.Clicking_Calender)

    # def get_current_date(self):
    #     return self.driver.find_element(*CalenderHandling.Clicking_Calender)


