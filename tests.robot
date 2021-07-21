*** Settings ***
Library    library/MyCurlLibrary.py


*** Test Cases ***
User requests a web page
    Request And Save Page From Url    https://klmp200.net/
    Page Reference Should Exist
    Check Page Requested