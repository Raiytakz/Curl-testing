.. code:: robotframework

    *** Settings ***
    Library    library/MyCurlLibrary.py


.. code:: robotframework

    *** Test Cases ***
    User requests a web page
        Request Page From Url    https://klmp200.net/
        Web Page Should Be Like    klmp200.html