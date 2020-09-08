from selenium import webdriver
import pytest

driver = None


@pytest.fixture
def setup(browser):
    global driver

    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path="D:\\PYTHON\\chromedriver.exe")

    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path="D:\\PYTHON\\geckodriver.exe")

    driver.maximize_window()

    # yield

    # driver.close()

    return driver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


def pytest_configure(config):
    config._metadata['Project Name'] = 'nopCommerce'
    config._metadata['Module Name'] = 'Customer'
    config._metadata['Tester'] = 'Ritesh'


@pytest.mark.optionhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
