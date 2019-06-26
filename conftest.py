import pytest
import sys

from selenium import webdriver
from selenium.webdriver.common.by import By


def pytest_addoption(parser):
    parser.addoption("--address", action="store", default="http://192.168.10.75/", help="Opencart web address")
    parser.addoption("--browser", action="store", default="firefox", help="Browser name")


@pytest.fixture(scope="session", autouse=True)
def driver(request):
    browser = request.config.getoption("--browser")
    if browser == 'firefox':
        capabilities = webdriver.DesiredCapabilities.FIREFOX.copy()
        capabilities['timeouts'] = {'implicit': 300000, 'pageLoad': 300000, 'script': 30000}
        capabilities['loggingPrefs'] = {'browser': 'ALL', 'client': 'ALL', 'driver': 'ALL',
                                        'performance': 'ALL', 'server': 'ALL'}
        profile = webdriver.FirefoxProfile()
        profile.set_preference('app.update.auto', False)
        profile.set_preference('app.update.enabled', False)
        profile.accept_untrusted_certs = True
        wd = webdriver.Firefox(firefox_profile=profile, capabilities=capabilities)
        wd.maximize_window()
    elif browser == 'chrome':
        capabilities = webdriver.DesiredCapabilities.CHROME.copy()
        capabilities['acceptSslCerts'] = True
        capabilities['acceptInsecureCerts'] = True
        wd = webdriver.Chrome(desired_capabilities=capabilities)
        wd.fullscreen_window()
    else:
        print('Unsupported browser!')
        sys.exit(1)
    yield wd
    wd.quit()


@pytest.fixture()
def login_page(driver, request):
    url = '/opencart/admin/'
    driver.get("".join([request.config.getoption("--address"), url]))


@pytest.fixture()
def open_product_page(driver):
    driver.find_element(By.ID, "input-username").send_keys("admin")
    driver.find_element(By.ID, "input-password").send_keys("admin")
    driver.find_element(By.CLASS_NAME, "btn.btn-primary").click()
    driver.find_element(By.CLASS_NAME, "close").click()
