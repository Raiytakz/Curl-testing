*** Settings ***
Library    library/MyCurlLibrary.py


*** Test Cases ***
User requests a web page
    Request Page From Url    https://klmp200.net/
    Web Page Should Be Like    klmp200.html