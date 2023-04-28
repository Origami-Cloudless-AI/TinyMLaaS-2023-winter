
*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${BROWSER}        headlessfirefox 
${DELAY}          0.10 seconds
${URL}            http://localhost:8501/Data


*** Keywords ***
Select dataset
    Wait Until Page Contains Element    //*[text()='Click to choose datasets']     20s
    Click Element     //*[text()='Click to choose datasets']

    Wait Until Page Contains     Choose dataset     20s
    Click Element    //*[text()="Choose dataset"]
    Wait Until Page Contains     Selected Person Detection     100s

Store unlabeled image
    Choose File    xpath:(//section[@data-testid='stFileUploadDropzone']//input)[last()]      ${EXECDIR}/data/1/1.png

    Wait Until Page Contains Element    xpath://*[text()="Click to see uploaded images"]     20s
    Click Element        xpath://*[text()="Click to see uploaded images"]

    Wait Until Page Contains Element    xpath://*[text()="Choose image"]
    Click Element   xpath://*[text()="Choose image"]
    Sleep     1.5s

    Wait Until Page Contains Element    xpath://*[text()="Unlabeled"] 
    Click Element   xpath://*[text()="Unlabeled"]
    Sleep     1.5s
    
    Wait Until Page Contains Element     xpath://*[text()="Store images"]
    Click Element   xpath://*[text()="Store images"]
    Sleep     10s

    Click Element   xpath://*[text()="Click to see uploaded images"]
    Sleep     10s

Give image 0 label
    Wait Until Page Contains Element    xpath://*[text()="Choose image"]
    Click Element   xpath://*[text()="Choose image"]
    Sleep     1.5s

    Wait Until Page Contains Element    xpath://*[text()="0"] 
    Click Element   xpath://*[text()="0"]
    Sleep     1.5s
    
    Wait Until Page Contains Element     xpath://*[text()="Store images"]
    Click Element   xpath://*[text()="Store images"]


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

    Select Dataset
    Close Browser

Test if image can be stored correctly

    Open Browser    about:blank    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}
    Go To           ${URL}
    Sleep     1.5s

    Wait Until Page Contains    Upload data
    Wait Until Page Contains Element    xpath:(//section[@data-testid='stFileUploadDropzone']//input)[last()]

    Select Dataset

    Choose File    xpath:(//section[@data-testid='stFileUploadDropzone']//input)[last()]      ${EXECDIR}/data/1/1.png    

    Wait Until Page Contains Element    xpath://*[text()="Click to see uploaded images"]
    Click Element        xpath://*[text()="Click to see uploaded images"]
    
    Give image 0 label

    Wait Until Page Contains    Images stored successfully!
    Close Browser

Test if labeling works for unlabeled images
    
    Open Browser    about:blank    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}
    Go To           ${URL}

    Select dataset