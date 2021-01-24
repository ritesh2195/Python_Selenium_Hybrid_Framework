from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from utilities.readProperties import ReadConfig

driver = None


@pytest.fixture(scope="class")
def setup(request):
    global driver

    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":

        driver = webdriver.Chrome(ChromeDriverManager().install())

    elif browser_name == "firefox":

        driver = webdriver.Firefox(executable_path='D:\\PYTHON\\geckodriver.exe')

    driver.maximize_window()

    driver.get(ReadConfig.getApplicationURL())

    driver.implicitly_wait(10)

    request.cls.driver = driver

    yield

    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


def pytest_configure(config):
    config._metadata['Project Name'] = 'nopCommerce'
    config._metadata['Module Name'] = 'Customer'
    config._metadata['Tester'] = 'Ritesh'


@pytest.mark.optionhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
