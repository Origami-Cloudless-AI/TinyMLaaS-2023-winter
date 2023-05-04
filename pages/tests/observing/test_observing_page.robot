*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${URL}            http://localhost:8501/Observing
${BROWSER}        firefox
${DELAY}          0.10 seconds
${DEVICE_URL}     http://localhost:8501/Device

*** Settings ***
Library    SeleniumLibrary


*** Keywords ***
Click Element After Wait
  [Arguments]  ${element}
  Wait Until Page Contains Element  ${element}   10s
  Click Element  ${element}

Select Relay Server
  Go to   ${DEVICE_URL}
  Wait Until Page Contains   IP address of the bridging server
  Input Text      xpath://input[@aria-label='IP address of the bridging server']     ${url}
  Click Element   xpath://*[text()="Add"]

*** Test Cases ***
Test if person detection observation fails with no relay

    Open Browser    about:blank    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}
    Go To           ${URL}

    Wait Until Page Contains   Person detection   20s
    Wait Until Page Contains   Relay server has not been selected.
    Close Browser

