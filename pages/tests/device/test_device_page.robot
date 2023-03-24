*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${BROWSER}        headlessfirefox
${DELAY}          0.10 seconds
${URL}            http://localhost:8501/Device


*** Keywords ***
Clear Text Field
  [Arguments]  ${inputField}
  press keys  ${inputField}  CTRL+a+BACKSPACE


*** Test Cases ***
Check Page Title
    Open Browser    ${URL}    ${BROWSER} 
    Sleep    1.5s
    ${title}=       Get Title
    Should Be Equal    ${title}    Device
    Close Browser


Device Page Register Connected Device Test
    Open Browser    about:blank    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}
    Go To           ${URL}
    

    ${register_button_exists} =  Run Keyword And Return Status    Element Should Be Visible    xpath://*[text()="register this device"]

    IF    ${register_button_exists}
        Wait Until Page Contains Element    xpath://*[text()="register this device"]
        Click Element    xpath://*[text()="register this device"]
        Wait Until Page Contains Element    xpath://input[@aria-label='Device name']
        
        Input Text      xpath://input[@aria-label='Device name']     TestDevice
        Input Text      xpath://input[@aria-label='Connection']      Wifi
        Input Text      xpath://input[@aria-label='Installer']       Installer
        Input Text      xpath://input[@aria-label='Compiler']        Compiler
        Input Text      xpath://input[@aria-label='Model']           Model
        Input Text      xpath://input[@aria-label='Description']     Test description
        Click Element    xpath://*[text()="Add"]
        Close Browser
    ELSE
        Log    No device connected currently
    END
    Close Browser

Device Page Add New Device Test
    Open Browser    about:blank    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}
    Go To           ${URL}
    
    Wait Until Page Contains Element    xpath://*[text()="register a new device"]
    Click Element    xpath://*[text()="register a new device"]

    Wait Until Page Contains Element    xpath://input[@aria-label='Device name']

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
    
    Wait Until Page Contains Element    xpath://*[text()="Modify"]
    Click Element    xpath://*[text()="Modify"]

    Wait Until Page Contains Element    xpath://input[@aria-label='Device name']

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
    
    Wait Until Page Contains Element    xpath://*[text()="Delete"]

    @{delete_buttons}=    Get WebElements    xpath://*[text()="Delete"]

    Wait Until Page Contains Element    ${delete_buttons[-1]}
    Click Element    ${delete_buttons[-1]}
    Close Browser



