
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

Test if selecting and uploading a dataset works
    
    Open Browser    about:blank    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}
    Go To           ${URL}

    Wait Until Page Contains Element    //*[text()='Click to choose datasets']     20s

    Click Element     //*[text()='Click to choose datasets']

    Wait Until Page Contains     Choose dataset     20s

    Click Element    //*[text()="Choose dataset"]

    Wait Until Page Contains    Store images    300s

    Click Element    //*[text()="Store images"]

    Wait Until Page Contains    Images stored successfully!    300s

    Close Browser

Test if image can be stored correctly

    Open Browser    about:blank    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}
    Go To           ${URL}
    Sleep     1.5s

    Wait Until Page Contains    Upload data
    Wait Until Page Contains Element    xpath:(//section[@data-testid='stFileUploadDropzone']//input)[last()]

    Choose File    xpath:(//section[@data-testid='stFileUploadDropzone']//input)[last()]      ${EXECDIR}/data/1/1.png
    Wait Until Page Contains    Photo uploaded successfully
    

    Wait Until Page Contains Element    xpath://*[text()="Click to see uploaded images"]
    Click Element        xpath://*[text()="Click to see uploaded images"]
    

    Wait Until Page Contains Element    xpath://*[text()="Choose image"]
    Click Element   xpath://*[text()="Choose image"]
    Sleep     1.5s


    Wait Until Page Contains Element    xpath://*[text()="0"] 
    Click Element   xpath://*[text()="0"]
    Sleep     1.5s
    
    Wait Until Page Contains Element     xpath://*[text()="Store images"]
    Click Element   xpath://*[text()="Store images"]

    Wait Until Page Contains    Images stored successfully!
    Close Browser

Test if labeling unlabeled images opens
    
    Open Browser    about:blank    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}
    Go To           ${URL}

    Wait Until Page Contains Element    //*[text()='Click to label unlabeled images']     20s

    Click Element     //*[text()='Click to label unlabeled images']

    Wait Until Page Contains     You haven't chosen any image     20s

    Close Browser
    