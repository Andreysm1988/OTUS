import pytest
import requests
import json


urls = ["https://dog.ceo/api/breeds/list/all",
        "https://dog.ceo/api/breed/affenpinscher/images/random",
        "https://dog.ceo/api/breeds/image/random"]


@pytest.fixture(params=urls)
def response(request):
    r = requests.get(request.param)
    return r


@pytest.mark.usefixtures("response")
def test_request(response):
    assert json.loads(response.text)['status'] == "success"
