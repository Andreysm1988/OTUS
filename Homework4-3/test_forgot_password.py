from selenium.webdriver.common.by import By


def test_forgot_password(driver, request):
    url = '/opencart/admin/'
    driver.get("".join([request.config.getoption("--address"), url]))
    driver.find_element(By.XPATH, "//*[@id='content']/div/div/div/div/div[2]/form/div[2]/span/a").click()
    e_mail = driver.find_element(By.NAME, "email")
    assert e_mail
