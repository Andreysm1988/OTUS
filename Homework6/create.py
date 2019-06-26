import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


@pytest.mark.usefixtures("open_product_page")
@pytest.mark.usefixtures("login_page")
def test_create(driver, delay=1):
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, "parent.collapsed")))
        driver.find_element(By.CLASS_NAME, "parent.collapsed").click()
    except (NoSuchElementException, TimeoutException):
        return False
    catalog_elements = driver.find_elements(By.TAG_NAME, "li")
    for catalog_element in catalog_elements:
        if catalog_element.text == "Products":
            catalog_element.click()
            break
    fluids = driver.find_elements(By.CLASS_NAME, "container-fluid")
    for fl in fluids:
        if "Products" in fl.text:
            action_fluid = fl
            break
    action_fluid.find_element(By.CLASS_NAME, "btn.btn-primary").click()
    driver.find_element(By.NAME, "product_description[1][name]").send_keys("TestProduct")
    driver.find_element(By.NAME, "product_description[1][meta_title]").send_keys("TagTest")
    driver.find_element(By.XPATH, "//*[@id='form-product']/ul/li[2]/a").click()
    driver.find_element(By.NAME, "model").send_keys("TestModel")
    driver.find_element(By.CLASS_NAME, "btn.btn-primary").click()
    success = driver.find_element(By.CLASS_NAME, "alert.alert-success.alert-dismissible")
    success_text = success.text.rstrip("\n×")
    assert success_text == "Success: You have modified products!"
