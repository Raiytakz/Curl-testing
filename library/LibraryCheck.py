import pytest
from pytest_mock import mocker
import requests
import MyCurlLibrary


curlLibrary = MyCurlLibrary.MyCurlLibrary()

class ResquestCurl:
    text = ""
    status_code = 0


def test_successful_request(mocker):
    page_url = "https://klmp200.net/"

    # SRR = SRR
    SRR = ResquestCurl()
    SRR.text = MyCurlLibrary.get_content_of_reference_of_page(page_url)
    SRR.status_code = 200

    mocker.patch(
        'MyCurlLibrary.MyCurlLibrary.request_and_save_page_from_url.self.request_page_from_url',
        return_value=SRR
        )
    # mocker.patch('MyCurlLibrary.MyCurlLibrary.request_and_save_page_from_url.self.save_html_using_name',
    #          return_value="")

    curlLibrary.request_page_from_url(page_url)
    assert curlLibrary._status == "Success"


def test_reference_page_not_existing():
    pass


def test_page_requested_different_from_reference():
    pass


def test_page_not_accessed():
    pass

