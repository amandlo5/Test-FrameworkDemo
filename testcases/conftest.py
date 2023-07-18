import pytest
from selenium import webdriver
import pytest_metadata

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
    elif browser == 'edge':
        driver = webdriver.Edge()
        driver.implicitly_wait(10)
        driver.maximize_window()
    else:
        print('driver is not correctly selected')

    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

#Pytest HTML report#

def pytest_configure(config):
    config._metadata = {
        "Tester": "Amol",
        "Project Name": "nop commerce",
        "Module" : "customers"
    }

@pytest.mark.optionalhookc
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)