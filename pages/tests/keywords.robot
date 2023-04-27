*** Variables ***
${BROWSER}        headlessfirefox
${URL}            http://localhost:8501
${DELAY}          0.10 seconds


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

