from selenium.webdriver.common.by import By


class Reports:
    def __init__(self, driver):
        self.driver = driver

    Clicking_Day_Close = (By.XPATH, "//span[normalize-space()='Day Close Report']")
    # driver.find_element(By.XPATH, "//span[normalize-space()='Day Close Report']").click()

    def clicked_day_close(self):
        return self.driver.find_element(*Reports.Clicking_Day_Close)



