*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${BROWSER}        chrome
${DELAY}          0.10 seconds
${URL}            http://localhost:8502/Training


*** Keywords ***


*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Test if training model trains the model
    
    Open Browser    about:blank    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}
    Go To           ${URL}
    Sleep     1.5s

    Click Element    xpath://*[text()="Train the model"]
    
    Sleep    50s
    Wait Until Page Contains  Model trained!


