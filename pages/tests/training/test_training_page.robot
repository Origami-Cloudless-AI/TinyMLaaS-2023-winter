*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${BROWSER}        headlessfirefox 
${DELAY}          0.10 seconds
${URL}            http://localhost:8501/Training
${DATA_URL}       http://localhost:8501/Data


*** Keywords ***
Clear Text Field
  [Arguments]  ${inputField}
  press keys  ${inputField}  CTRL+a+BACKSPACE

Click Element After Wait
  [Arguments]  ${element}
  Wait Until Page Contains Element  ${element}
  Click Element  ${element}

Select First Dataset
   Go to   ${DATA_URL}
   Click Element After Wait    xpath://*[text()="Choose dataset"]
   Wait Until Page Contains    Person Detection dataset selected    200s

Select First Model 
   Click Element After Wait    xpath://*[text()="Model"] 
   Click Element After Wait    xpath=//div[contains(text(), 'Face Recognition')]
   Wait Until Page Contains    You have selected: Modified LBPH submodel under Face Recognition model 
   Click Element    xpath://*[text()="Select"]
   Wait Until Page Contains  Your selections have been saved


*** Test Cases ***
Check Page Title
    Open Browser    ${URL}    ${BROWSER} 
    Sleep    1.5s
    Wait Until Page Contains    Training    300s
    Close Browser


Training fails with no dataset
    Open Browser    ${URL}    ${BROWSER} 
    Wait Until Page Contains   No dataset was selected   20s
    Close Browser

Training fails with no model
    Open Browser    ${URL}    ${BROWSER}
    Select First Dataset
    Click Element   xpath://*[text()="Training"]
    Wait Until Page Contains   No model was selected   20s
    Close Browser

Run steps to train model test
    Open Browser    about:blank    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

    Select First Dataset
    Select First Model
    Click Element   xpath://*[text()="Training"]      #"Go To" wouldn't update session_state

    Wait Until Page Contains Element    xpath://input[@aria-label='Enter the number of epochs']   20s

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
