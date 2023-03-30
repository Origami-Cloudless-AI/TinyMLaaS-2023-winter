
*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${BROWSER}        headlessfirefox 
${DELAY}          0.10 seconds
${URL}            http://localhost:8501/Installing


*** Keywords ***


*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Test if page contains "TinyML Install" 
    
    Open Browser    about:blank    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}
    Go To           ${URL}

    Wait Until Page Contains     TinyML Install   20s
    Close Browser
