
*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${BROWSER}        chrome
${DELAY}          0.10 seconds
${URL}            http://localhost:8501/Installing


*** Keywords ***


*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Test if selecting a category and model works
    
    Open Browser    about:blank    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}
    Go To           ${URL}
    Sleep     1.5s

    Wait Until Page Contains     TinyML Install
    Close Browser
