import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("login_page")
def test_login_fail(driver):
    driver.find_element(By.ID, "input-username").send_keys("admin")
    driver.find_element(By.ID, "input-password").send_keys("111")
    driver.find_element(By.CLASS_NAME, "btn.btn-primary").click()
    warning = driver.find_element(By.CLASS_NAME, "alert.alert-danger.alert-dismissible")
    warning_text = warning.text.rstrip("\n×")
    assert warning_text == "No match for Username and/or Password."
