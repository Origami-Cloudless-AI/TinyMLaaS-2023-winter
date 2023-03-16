*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${BROWSER}        headlessfirefox 
${DELAY}          0.10 seconds
${URL}            http://localhost:8501/Model


*** Keywords ***


*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Test if selecting a category and model works
    
    Open Browser    about:blank    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}
    Go To           ${URL}

    Wait Until Page Contains Element    xpath=//div[contains(text(), 'Object Detection')]    10s 

    Click Element    xpath=//div[contains(text(), 'Object Detection')]

    Wait Until Page Contains     You have selected: Matias's R-CNN model submodel under Object Detection model

    Click Element    xpath://*[text()="Select"]

    Wait Until Page Contains  Your selections have been saved

    Close Browser


