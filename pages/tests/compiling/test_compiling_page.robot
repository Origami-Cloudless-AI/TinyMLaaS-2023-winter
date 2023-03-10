
*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${BROWSER}        chrome
${DELAY}          0.10 seconds
${URL}            http://localhost:8501/Compiling


*** Keywords ***


*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Test if compiling page loads correctly

    Open Browser    about:blank    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}
    Go To           ${URL}
    Sleep     1.5s

    Wait Until Page Contains     ML Compilation
    Close Browser
