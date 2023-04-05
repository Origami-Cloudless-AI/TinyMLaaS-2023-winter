*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${BROWSER}        headlessfirefox 
${DELAY}          0.10 seconds
${URL}            http://localhost:8501/Training


*** Keywords ***
Clear Text Field
  [Arguments]  ${inputField}
  press keys  ${inputField}  CTRL+a+BACKSPACE



*** Test Cases ***
Check Page Title
    Open Browser    ${URL}    ${BROWSER} 
    Sleep    1.5s
    Wait Until Page Contains    Training    300s
    Close Browser


Run steps to train model test
    Open Browser    about:blank    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}
    Go To           ${URL}

    Wait Until Page Contains Element    xpath://input[@aria-label='Enter the number of epochs']

    Clear Text Field    xpath://input[@aria-label='Enter the number of epochs']
    Input Text      xpath://input[@aria-label='Enter the number of epochs']     5
    Press Keys     xpath://input[@aria-label='Enter the number of epochs']    ENTER
    

    Wait Until Page Contains Element    xpath://input[@aria-label='Enter the batch size']
    Clear Text Field    xpath://input[@aria-label='Enter the batch size']
    Input Text      xpath://input[@aria-label='Enter the batch size']     28
    Press Keys     xpath://input[@aria-label='Enter the batch size']    ENTER

    
    Wait Until Page Contains Element    xpath://input[@aria-label='Enter image width']
    Clear Text Field    xpath://input[@aria-label='Enter image width']
    Input Text      xpath://input[@aria-label='Enter image width']     180
    Press Keys     xpath://input[@aria-label='Enter image width']    ENTER

    Wait Until Page Contains Element    xpath://input[@aria-label='Enter image height']
    Clear Text Field    xpath://input[@aria-label='Enter image height']
    Input Text      xpath://input[@aria-label='Enter image height']     180
    Press Keys     xpath://input[@aria-label='Enter image height']    ENTER
   
    Wait Until Page Contains Element    xpath=//div[contains(text(), 'Sparse Categorical crossentropy')]
    Click Element    xpath=//div[contains(text(), 'Sparse Categorical crossentropy')]
    
    Wait Until Page Contains Element    xpath://*[text()="Train"]
    Click Element    xpath://*[text()="Train"]
    Wait Until Page Contains  Model trained successfully!    300s

    Close Browser
