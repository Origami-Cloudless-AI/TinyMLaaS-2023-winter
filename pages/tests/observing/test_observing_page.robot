*** Settings ***
Library           SeleniumLibrary
Resource          pages/tests/keywords.robot

*** Variables ***
${URL}            http://localhost:8501/Observing
${BROWSER}        headlessfirefox
${DELAY}          0.10 seconds


*** Settings ***
Library    SeleniumLibrary


*** Keywords ***
Click Element After Wait
  [Arguments]  ${element}
  Wait Until Page Contains Element  ${element}   10s
  Click Element  ${element}

Select Relay Server
  [Arguments]   ${url}
  Click Element After Wait   xpath://*[text()="Device"]
  Wait Until Page Contains   IP address of the bridging server
  Input Text      xpath://input[@aria-label='IP address of the bridging server']     ${url}
  Click Element   xpath://*[text()="Add"]

*** Test Cases ***
Test if observing page loads correctly    

    Open Browser    about:blank    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}
    Go To           ${URL}

    Wait Until Page Contains     Device Observing Dashboard
    Close Browser

Test if person detection observation fails with no relay

    Open Browser    about:blank    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}
    Go To           ${URL}
    Wait Until Page Contains   Relay server has not been selected.
    Close Browser

Test if person detection observation fails with no device

    Open Browser    about:blank    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}
    Go To           ${URL}
    
    Select Relay Server   http://0.0.0.0
    Click Element   xpath://*[text()="Observing"] 

    Click Element After Wait    xpath://*[text()="Start"]
    Wait Until Page Contains   Unable to read from device.
    Close Browser
