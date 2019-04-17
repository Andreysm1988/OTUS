import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("login_page")
def test_login_pass(driver):
    driver.find_element(By.ID, "input-username").send_keys("admin")
    driver.find_element(By.ID, "input-password").send_keys("admin")
    driver.find_element(By.CLASS_NAME, "btn.btn-primary").click()
    warning = driver.find_element(By.CLASS_NAME, "close")
    assert warning
