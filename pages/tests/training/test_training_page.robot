*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${BROWSER}        chrome
${DELAY}          0.10 seconds
${URL}            http://localhost:8501/Training


*** Keywords ***
Clear Text Field
  [Arguments]  ${inputField}
  press keys  ${inputField}  CTRL+a+BACKSPACE



*** Test Cases ***
Check Page Title
    Open Browser    ${URL}    chrome
    Sleep    1.5s
    ${title}=       Get Title
    Should Be Equal    ${title}    Training
    Close Browser


Run steps to train model test
    Open Browser    about:blank    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}
    Go To           ${URL}

    Sleep     1.5s
    Clear Text Field    xpath://input[@aria-label='Enter the number of epochs']
    Input Text      xpath://input[@aria-label='Enter the number of epochs']     5
    Press Keys     xpath://input[@aria-label='Enter the number of epochs']    ENTER
    
    Sleep     0.5s

    Clear Text Field    xpath://input[@aria-label='Enter the batch size']
    Input Text      xpath://input[@aria-label='Enter the batch size']     28
    Press Keys     xpath://input[@aria-label='Enter the batch size']    ENTER

    Sleep     0.5s

    Clear Text Field    xpath://input[@aria-label='Enter image width']
    Input Text      xpath://input[@aria-label='Enter image width']     180
    Press Keys     xpath://input[@aria-label='Enter image width']    ENTER

    Sleep     0.5s
    
    Clear Text Field    xpath://input[@aria-label='Enter image height']
    Input Text      xpath://input[@aria-label='Enter image height']     180
    Press Keys     xpath://input[@aria-label='Enter image height']    ENTER
    Sleep     0.5s
    
    Click Element    xpath=//div[contains(text(), 'Sparse Categorical crossentropy')]

    Sleep     0.5s

    Click Element    xpath://*[text()="Train"]

    Sleep    100s

    Wait Until Page Contains  Model trained successfully!

    Close Browser