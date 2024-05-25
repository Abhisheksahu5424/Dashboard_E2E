import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="This to Change the Browser" # pytest --browser_name chrome
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        service_obj = Service()
        webdriver.Chrome(service=service_obj)

        url = "https://reports.parkzap.com/login"
        driver = webdriver.Chrome()
        driver.get(url)
        time.sleep(2)
        print(driver.title)
        print(driver.current_url)
        driver.maximize_window()

    elif browser_name == "firefox":
        print("Firefox")
    elif browser_name == "IE":
        print("IE")

    request.cls.driver = driver

    yield
    driver.close()