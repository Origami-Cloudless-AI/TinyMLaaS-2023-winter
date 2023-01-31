*** Settings ***
Library   SeleniumLibrary
Library   Process

Suite Setup         Start the webserver

Suite Teardown      Stop the webserver

*** Keywords ***
Start the webserver
    Log To Console  start
    ${process}=     Start Process       python3     -m      coverage    run     --source    src    -m      streamlit    run     TinyMLaaS.py     --server.port       5000    --server.headless   true

    Set suite variable    ${process}
    Log To Console     ${process}
    sleep  2s

Stop the webserver
    Log To Console  end
    Terminate Process    ${process}

*** Variables ***
${URL}             http://localhost:5000/
${BROWSER}         headlessfirefox

*** Test Cases ***
test 1
    Log To Console  open frontpage
    Open Browser  ${URL}  browser=${BROWSER}
    Wait Until Page Contains    TinyML as-a-Service
    Page Should Contain     TinyMLaaS
    Click Element       //*[text()='Device']
    sleep  2s
    Page Should Contain    List all registered devices
    Click Element       //*[text()='TinyMLaaS']
    sleep  2s
    Page Should Contain    TinyML as-a-Service
    Close Browser

test 2
    Log To Console  open device
    Open Browser  ${URL}  browser=${BROWSER}
    Wait Until Page Contains    TinyML as-a-Service
    Page Should Contain    TinyMLaaS
    Click Element       //*[text()='Device']
    sleep  2s
    Page Should Contain    Register a device
    Close Browser

test 3
    Log To Console  open data
    Open Browser  ${URL}  browser=${BROWSER}
    Wait Until Page Contains    TinyML as-a-Service
    Page Should Contain    TinyMLaaS
    Click Element       //*[text()='Data']
    sleep  2s
    Page Should Contain    Upload data
    Close Browser

test 4
    Log To Console  open model
    Open Browser  ${URL}  browser=${BROWSER}
    Wait Until Page Contains    TinyML as-a-Service
    Page Should Contain    TinyMLaaS
    Click Element       //*[text()='Model']
    sleep  2s
    Page Should Contain    Which models are needed
    Close Browser

test 5
    Log To Console  open training
    Open Browser  ${URL}  browser=${BROWSER}
    Wait Until Page Contains    TinyML as-a-Service
    Page Should Contain    TinyMLaaS
    Click Element       //*[text()='Training']
    sleep  2s
    Page Should Contain    Storing data
    Close Browser

test 6
    Log To Console  open compiling
    Open Browser  ${URL}  browser=${BROWSER}
    Wait Until Page Contains    TinyML as-a-Service
    Page Should Contain    TinyMLaaS
    Click Element       //*[text()='Compiling']
    sleep  2s
    Page Should Contain    Compiling Hello World TinyML model
    Close Browser

test 7
    Log To Console  open installing
    Open Browser  ${URL}  browser=${BROWSER}
    Wait Until Page Contains    TinyML as-a-Service
    Page Should Contain    TinyMLaaS
    Click Element       //*[text()='Installing']
    sleep  2s
    Page Should Contain    Installing Hello World binary in Container
    Close Browser

test 8
    Log To Console  open observing
    Open Browser  ${URL}  browser=${BROWSER}
    Wait Until Page Contains    TinyML as-a-Service
    Page Should Contain    TinyMLaaS
    Click Element       //*[text()='Observing']
    sleep  2s
    Page Should Contain    Real-Time / Live Data Science Dashboard
    Close Browser