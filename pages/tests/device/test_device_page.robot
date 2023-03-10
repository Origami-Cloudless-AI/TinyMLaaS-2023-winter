*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${BROWSER}        chrome
${DELAY}          0.10 seconds
${URL}            http://localhost:8501/Device


*** Keywords ***
Clear Text Field
  [Arguments]  ${inputField}
  press keys  ${inputField}  CTRL+a+BACKSPACE



*** Test Cases ***
Check Page Title
    Open Browser    ${URL}    chrome
    Sleep    1.5s
    ${title}=       Get Title
    Should Be Equal    ${title}    Device
    Close Browser


Device Page Add New Device Test
    Open Browser    about:blank    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}
    Go To           ${URL}
    Sleep     1.5s
    Click Element    xpath://*[text()="Add"]
    Sleep     1.5s
    Input Text      xpath://input[@aria-label='Device name']     TestDevice
    Input Text      xpath://input[@aria-label='Connection']      Wifi
    Input Text      xpath://input[@aria-label='Installer']       Installer
    Input Text      xpath://input[@aria-label='Compiler']        Compiler
    Input Text      xpath://input[@aria-label='Model']           Model
    Input Text      xpath://input[@aria-label='Description']     Test description
    Click Element    xpath://*[text()="Add"]
    Close Browser

Device Page Modify One Device Test
    Open Browser    about:blank    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}
    Go To           ${URL}
    Sleep     1.5s
    Click Element    xpath://*[text()="Modify"]
    Sleep     1.5s
    Clear Text Field    xpath://input[@aria-label='Device name']
    Clear Text Field    xpath://input[@aria-label='Connection']
    Clear Text Field    xpath://input[@aria-label='Installer']
    Clear Text Field    xpath://input[@aria-label='Compiler']
    Clear Text Field    xpath://input[@aria-label='Model']
    Clear Text Field    xpath://input[@aria-label='Description']

    Input Text      xpath://input[@aria-label='Device name']      Modified_Test
    Input Text      xpath://input[@aria-label='Connection']       Modified_Test
    Input Text      xpath://input[@aria-label='Installer']        Modified_Test 
    Input Text      xpath://input[@aria-label='Compiler']         Modified_Test
    Input Text      xpath://input[@aria-label='Model']            Modified_Test07
    Input Text      xpath://input[@aria-label='Description']      Modified_Test
    Click Element    xpath://*[text()="Modify Device"]
    Wait Until Element Is Visible    xpath://*[text()="Modified_Test"]
    Close Browser

Device Page Delete Last Device in the List Test
    Open Browser    about:blank    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}
    Go To           ${URL}
    Sleep     1.5s

    
    @{delete_buttons}=    Get WebElements    xpath://*[text()="Delete"]
    Click Element    ${delete_buttons[-1]}
    Close Browser