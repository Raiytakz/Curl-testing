import pytest
import requests
import MyCurlLibrary
import pytest_mock


curlLibrary = MyCurlLibrary.MyCurlLibrary()


class FakeResquestResponse:
    text = ""
    status_code = 0


global_page_url = "https://medium.com/analytics-vidhya/mocking-in-python-with-pytest-mock-part-i-6203c8ad3606"


def test_request_success(mocker):
    page_url = global_page_url

    FRR = FakeResquestResponse()
    FRR.status_code = 200

    mocker.patch("MyCurlLibrary.io.open")
    mocker.patch("MyCurlLibrary.requests.get", return_value=FRR)
    spy_io_save = mocker.spy(MyCurlLibrary.io, "open")

    curlLibrary.request_and_save_page_from_url(page_url)

    assert curlLibrary._status == "Success"
    assert spy_io_save.call_count == 1


def test_no_reference_page(mocker):
    page_url = global_page_url

    mocker.patch("MyCurlLibrary.io.open")
    mocker.patch("MyCurlLibrary.os.path.exists", side_effect=FileNotFoundError)
    spy_os_path = mocker.spy(MyCurlLibrary.os.path, "exists")

    try:
        curlLibrary.page_reference_should_exist()
        raise Exception("The reference page should not have been founded")
    except FileNotFoundError:
        # This is the desired result
        pass

    assert spy_os_path.call_count == 1


def test_page_requested_different_from_reference(mocker):
    page_url = global_page_url

    mocker.patch("MyCurlLibrary.io.open")
    mocker.patch("MyCurlLibrary.get_content_of_path", side_effect=[True, False])

    curlLibrary.request_and_save_page_from_url(page_url)
    try:
        curlLibrary.web_page_should_be_like(curlLibrary._site_name)
        raise Exception("The pages shoud be different")
    except AssertionError:
        # This is the desired result
        pass


def test_page_not_found(mocker):
    page_url = global_page_url

    FRR = FakeResquestResponse()
    FRR.status_code = 404

    mocker.patch("MyCurlLibrary.io.open")
    mocker.patch("MyCurlLibrary.requests.get", return_value=FRR)
    spy_io_save = mocker.spy(MyCurlLibrary.io, "open")

    try:
        curlLibrary.request_and_save_page_from_url(page_url)
        raise Exception
    except AssertionError:
        # This is the desired result
        pass

    assert curlLibrary._status == "Failure"
