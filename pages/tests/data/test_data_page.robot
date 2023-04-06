
*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${BROWSER}        headlessfirefox 
${DELAY}          0.10 seconds
${URL}            http://localhost:8501/Data


*** Keywords ***


*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Test if page contains "Upload data" 
    
    Open Browser    about:blank    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}
    Go To           ${URL}

    Wait Until Page Contains     Upload data   20s
    Close Browser

#Test if selecting and uploading a dataset works
    
    #Open Browser    about:blank    ${BROWSER}
    #Maximize Browser Window
    #Set Selenium Speed  ${DELAY}
    #Go To           ${URL}

    #Wait Until Page Contains Element    //*[text()='Click to choose datasets']     20s

    #Click Element     //*[text()='Click to choose datasets']

    #Wait Until Page Contains     Choose dataset     20s

    #Click Element    //*[text()="Choose dataset"]

    #Wait Until Page Contains  Uploaded dataset     20s

    #Wait Until Page Contains    Click to see uploaded dataset    20s

    #Click Element    //*[text()='Click to see uploaded dataset']

    #Close Browser

