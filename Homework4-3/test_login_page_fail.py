from selenium.webdriver.common.by import By


def test_login_fail(driver, request):
    url = '/opencart/admin/'
    driver.get("".join([request.config.getoption("--address"), url]))
    driver.find_element(By.ID, "input-username").send_keys("admin")
    driver.find_element(By.ID, "input-password").send_keys("111")
    driver.find_element(By.CLASS_NAME, "btn.btn-primary").click()
    warning = driver.find_element(By.CLASS_NAME, "alert.alert-danger.alert-dismissible")
    #warning_text = warning.text.rstrip("\n*'")
    assert warning
    #assert warning_text == "No match for Username and/or Password."
