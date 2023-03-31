
*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${BROWSER}        headlessfirefox
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

    Wait Until Page Contains     ML Compilation   20s
    Close Browser
