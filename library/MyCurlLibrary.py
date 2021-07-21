import requests
from robot.api.deco import keyword
import os
import re


class MyCurlLibrary:
    def __init__(self):
        self._status = "Fail"
        self._html_page = ""
        self._site_name = ""

        self._current_dir = os.path.join(os.path.dirname(__file__), "..")
        self._site_dir = os.path.join(self._current_dir, "site")

    @keyword("Request Page From Url")
    def request_page_from_url(self, desired_url):
        self._html_page = ""
        self._site_name = get_domain_name_from(desired_url)

        response = requests.get(desired_url)

        if response.status_code == 200:
            self._status = "Success"
            self._html_page = response.text
            f = open(os.path.join(self._site_dir, self._site_name + "_response.html"), "w+")
            f.write(self._html_page)

        else:
            self._status = "Failure"
            raise AssertionError("The page was not accessed")

    def web_page_should_be_like(self, saved_page):
        path_sp = os.path.join(self._site_dir, saved_page)
        with open(path_sp, "r") as sp:
            sp_html = sp.read()

        path_res = os.path.join(self._site_dir, self._site_name + "_response.html")
        with open(path_res, "r") as res:
            res_html = res.read()

        if sp_html != res_html:
            raise AssertionError("The page downloaded wasn't the one asked")


def get_domain_name_from(url):
    match_https = re.compile(r"^(https?\:\/\/)")
    url_no_https = re.sub(match_https, "", url)
    dn_from_url = re.sub(r"/", "", url_no_https)
    return dn_from_url


# my_url = "https://klmp200.net/"
# mycurl = MyCurlLibrary()
# mycurl.request_page_from_url(my_url)
