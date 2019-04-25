import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("open_product_page")
@pytest.mark.usefixtures("login_page")
def test_create(driver):
    elements = driver.find_elements(By.CLASS_NAME, "parent.collapsed")
    for element in elements:
        if element.text == "Catalog":
            catalog = element
            break
    catalog.click()
    catalog_elements = driver.find_elements(By.TAG_NAME, "li")
    for catalog_element in catalog_elements:
        if catalog_element.text == "Products":
            catalog_element.click()
            break
    driver.find_element(By.NAME, "filter_name").send_keys("Test")
    driver.find_element(By.ID, "button-filter").click()
    driver.find_element(By.XPATH, "//*[@id='form-product']/div/table/tbody/tr/td[8]/a").click()
    driver.find_element(By.NAME, "product_description[1][name]").clear()
    driver.find_element(By.NAME, "product_description[1][name]").send_keys("TestProduct123")
    driver.find_element(By.CLASS_NAME, "btn.btn-primary").click()
    success = driver.find_element(By.CLASS_NAME, "alert.alert-success.alert-dismissible")
    success_text = success.text.rstrip("\n×")
    assert success_text == "Success: You have modified products!"
