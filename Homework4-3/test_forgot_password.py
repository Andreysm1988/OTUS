import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("login_page")
def test_forgot_password(driver):
    driver.find_element(By.XPATH, "//*[@id='content']/div/div/div/div/div[2]/form/div[2]/span/a").click()
    e_mail = driver.find_element(By.CLASS_NAME, "panel-title")
    e_mail_text = e_mail.text.rstrip("\n")
    assert e_mail_text == "Forgot Your Password?"
