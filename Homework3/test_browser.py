def test_title(driver, request):
    url = '/opencart/'
    driver.get("".join([request.config.getoption("--address"), url]))
    assert "Your Store" in driver.title
