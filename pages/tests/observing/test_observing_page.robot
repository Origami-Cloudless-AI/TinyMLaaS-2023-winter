
*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${BROWSER}        chrome
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
    Sleep     1.5s

    Wait Until Page Contains     Device Observing Dashboard
    Close Browser
