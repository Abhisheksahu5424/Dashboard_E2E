import datetime
import time

import pytest
import self
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from pageObjects.CalenderHandling import CalenderHandling
from pageObjects.Reports import Reports
from pageObjects.LoginPage import LoginPage
from pageObjects.PostLogin import InternalFunc
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_dashboard_login(self):
        email_id = LoginPage(self.driver)
        email_id.entering_email().send_keys("abhishek.sahu@stackfusion.io")
        # Sending the User Email ID
        # self.driver.find_element(By.XPATH, "//input[@placeholder='Email']").send_keys("abhishek.sahu@stackfusion.io")
        print("Sending User ID")

        password = LoginPage(self.driver)
        password.entering_pass().send_keys("Harrypotter@2023")

        # self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("Harrypotter@2023")
        print("Sending User Pass")

        # self.driver.find_element(By.XPATH, "//button[normalize-space()='Sign in']").click()
        login = LoginPage(self.driver)
        login.clicking_login_button().click()
        print("Clicking on Sign IN Button")
        time.sleep(2)

    def test_post_login(self):
        # driver.find_element(By.XPATH, "(//span[@class='p-dropdown-trigger-icon p-clickable pi pi-chevron-down'])[
        # 1]").click()
        dropdown = InternalFunc(self.driver)
        dropdown.drop_down().click()
        print("Clicking on Dropdown")
        time.sleep(2)

        # driver.find_element(By.CLASS_NAME, "p-dropdown-filter").send_keys("Ahm")
        site_keyword = InternalFunc(self.driver)
        site_keyword.send_site_name().send_keys("Ahm")
        print("Clicking on dropdown and sending the input")
        time.sleep(2)

    def test_select_sites(self):
        select_site = InternalFunc(self.driver)
        sites = select_site.selecting_sites()
        # sites = driver.find_elements(By.CSS_SELECTOR, "li[class='p-dropdown-item']")
        print(len(sites))
        time.sleep(2)

        assert len(sites) > 1, "No sites found in the dropdown"

        found_site = False
        for site_list in sites:
            if site_list.text == "Ahmedabad Airport T2":
                found_site = True
                print(found_site)
                site_list.click()
                time.sleep(2)
                break

        # Assert that "Ahmedabad Airport T2" was found
        assert found_site, "Site 'Ahmedabad Airport T2' not found in the dropdown"
        print("Site 'Ahmedabad Airport T2' selected successfully")

    def test_day_close_report(self):
        day_close = Reports(self.driver)
        day_close.clicked_day_close().click()

    def test_get_date(self):
        handle_calender = CalenderHandling(self.driver)
        current_date = handle_calender.calender().click()
        print(current_date)
        time.sleep(4)



