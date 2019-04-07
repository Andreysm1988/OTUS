import pytest
import requests


urls = ["https://dog.ceo/api/breeds/list/all",
        "https://dog.ceo/api/breed/affenpinscher/images/random",
        "https://dog.ceo/dog-api/about",
        "https://dog.ceo/api/breeds/image/random",
        "https://dog.ceo/dog-api/documentation/breed",
        "https://dog.ceo/dog-api/documentation/sub-breed",
        "https://dog.ceo/dog-api/breeds-list",
        "https://www.openbrewerydb.org/",
        "https://cdnjs.com/api",
        "https://cdnjs.com/about",
        "https://cdnjs.com/",
        "https://cdnjs.com/libraries"]


@pytest.fixture(params=urls)
def response(request):
    r = requests.get(request.param)
    return r


@pytest.mark.usefixtures("response")
def test_headers(response):
    assert response.headers['Content-Type'] == "application/json" or "text/html"
