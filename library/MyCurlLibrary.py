import requests
from robot.api.deco import keyword
import os
import re
import io


CURR_DIR = os.path.join(os.path.dirname(__file__), "..")
SITES_DIR = os.path.join(CURR_DIR, "sites")

class MyCurlLibrary:
    def __init__(self):
        self._status = "Fail"
        self._html_page = ""
        self._site_name = ""

        self._current_dir = CURR_DIR
        self._site_dir = SITES_DIR

    def request_and_save_page_from_url(self, desired_url):
        request_response = self.request_page_from_url(desired_url)
        if request_response.status_code == 200:
            self._status = "Success"
            self._html_page = request_response.text
            save_html_using_name(self._site_name + "_response.html", request_response)

        else:
            self._status = "Failure"
            raise AssertionError("The page was not accessed")

    def request_page_from_url(self, desired_url):
        self._html_page = ""
        self._site_name = get_domain_name_from_url(desired_url)
        response = requests.get(desired_url)
        return response

    def web_page_should_be_like(self, reference_page):
        path_sp = os.path.join(self._site_dir, reference_page + ".html")
        sp_html = get_content_of_path(path_sp)

        path_res = os.path.join(self._site_dir, self._site_name + "_response.html")
        res_html = get_content_of_path(path_res)

        if sp_html != res_html:
            raise AssertionError("The page downloaded wasn't the one asked")

    def check_page_requested(self):
        self.web_page_should_be_like(self._site_name)

    def page_reference_should_exist(self):
        path_ref_page = os.path.join(self._site_dir, self._site_name + ".html")
        if os.path.exists(path_ref_page) == False:
            raise AssertionError("File to compare does not exist")




def get_content_of_reference_of_page(desired_url):
    dn_from_url = get_domain_name_from_url(desired_url)
    path_to_get = os.path.join(SITES_DIR, dn_from_url+".html")
    return get_content_of_path(path_to_get)


def get_domain_name_from_url(url):
    match_https = re.compile(r"^(http.*?\:\/\/)")
    url_no_https = re.sub(match_https, "", url)
    dn_from_url = re.sub(r"/.?", "", url_no_https)
    return dn_from_url

def get_content_of_path(path_to_get):
    with io.open(path_to_get, "r", encoding="utf8") as fd:
        fd_content = fd.read()
    return fd_content

def save_html_using_name(name_site, request_response):
    path_to_save_file = os.path.join(SITES_DIR, name_site)
    with io.open(path_to_save_file, "w+", encoding="utf8") as f:
        f.write(request_response.text)


# my_url = "https://klmp200.net/"
# mycurl = MyCurlLibrary()
# response = mycurl.request_page_from_url(my_url)
# mycurl.save_html_using_name(get_domain_name_from_url(my_url) + ".html", response)
