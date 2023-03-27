
*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${BROWSER}        headlessfirefox 
${DELAY}          0.10 seconds
${URL}            http://localhost:8501/Observing


*** Keywords ***


*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Test if observing page loads correctly    

    Open Browser    about:blank    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}
    Go To           ${URL}

    Wait Until Page Contains     Device Observing Dashboard
    Close Browser

Test if person detection observation fails with no device

    Open Browser    about:blank    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}
    Go To           ${URL}
    Wait Until Page Contains Element    xpath://*[text()="Start"]   15s
    Click Element    xpath://*[text()="Start"]
    Wait Until Page Contains   Unable to read from device.
    Close Browser
