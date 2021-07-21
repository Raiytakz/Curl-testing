import pytest
import requests
import MyCurlLibrary


curlLibrary = MyCurlLibrary.MyCurlLibrary()


def test_successful_request():
    curlLibrary.request_page_from_url("https://klmp200.net/")
    assert curlLibrary._status == "Success"


def test_correct_response():
    curlLibrary.request_page_from_url("https://klmp200.net/")
    desired_html_page = requests.get("https://klmp200.net/").text

    assert curlLibrary._html_page == desired_html_page


# import os
# path = r"C:\Users\m.salaun\Documents\Curl Testing\klmp200.html"
# fd = open(path, "w")
# str =  requests.get("https://klmp200.net/").text
# fd.write(str)
