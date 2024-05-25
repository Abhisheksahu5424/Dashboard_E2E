from selenium.webdriver.common.by import By


class InternalFunc:
    def __init__(self, driver):
        self.driver = driver

# driver.find_element(By.XPATH,"(//span[@class='p-dropdown-trigger-icon p-clickable pi pi-chevron-down'])[1]").click()
    DropDown = (By.XPATH, "(//span[@class='p-dropdown-trigger-icon p-clickable pi pi-chevron-down'])[1]")

    # driver.find_element(By.CLASS_NAME, "p-dropdown-filter").send_keys("Ahm")
    SendSitesName = (By.CLASS_NAME, "p-dropdown-filter")

    # sites = driver.find_elements(By.CSS_SELECTOR, "li[class='p-dropdown-item']")
    Select_Sites = (By.CSS_SELECTOR, "li[class='p-dropdown-item']")

    def drop_down(self):
        return self.driver.find_element(*InternalFunc.DropDown)

    def send_site_name(self):
        return self.driver.find_element(*InternalFunc.SendSitesName)

    def selecting_sites(self):
        return self.driver.find_elements(*InternalFunc.Select_Sites)

