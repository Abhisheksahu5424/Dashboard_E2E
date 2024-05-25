from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    # self.driver.find_element(By.XPATH, "//input[@placeholder='Email']").send_keys("abhishek.sahu@stackfusion.io")
    Email_ID = (By.XPATH, "//input[@placeholder='Email']")

    # self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("Harrypotter@2023")
    PassWord = (By.XPATH, "//input[@placeholder='Password']")
    # self.driver.find_element(By.XPATH, "//button[normalize-space()='Sign in']").click()
    Login_Button = (By.XPATH, "//button[normalize-space()='Sign in']")

    def entering_email(self):
        return self.driver.find_element(*LoginPage.Email_ID)

    def entering_pass(self):
        return self.driver.find_element(*LoginPage.PassWord)

    def clicking_login_button(self):
        return self.driver.find_element(*LoginPage.Login_Button)


