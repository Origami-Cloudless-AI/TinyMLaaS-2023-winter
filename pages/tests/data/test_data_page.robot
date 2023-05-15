
*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${BROWSER}        headlessfirefox 
${DELAY}          0.10 seconds
${URL}            http://localhost:8501/Data


*** Keywords ***
Select dataset
    Wait Until Page Contains     Choose dataset     20s
    Click Element    //*[text()="Choose dataset"]
    Wait Until Page Contains     Person Detection dataset selected     100s

Store unlabeled image
    Choose File    xpath:(//section[@data-testid='stFileUploadDropzone']//input)[last()]      ${EXECDIR}/data/1/1.png

    Wait Until Page Contains Element    xpath://*[text()="Click to see uploaded images"]     20s
    Click Element        xpath://*[text()="Click to see uploaded images"]

    Wait Until Page Contains Element    xpath://*[text()="Choose image"]
    Click Element   xpath://*[text()="Choose image"]

    Wait Until Page Contains Element    xpath://*[text()="Unlabeled"] 
    Click Element   xpath://*[text()="Unlabeled"]
    
    Wait Until Page Contains Element     xpath://*[text()="Store images"]
    Click Element   xpath://*[text()="Store images"]

    Click Element   xpath://*[text()="Click to see uploaded images"]

Give image 0 label
    Wait Until Page Contains Element    xpath://*[text()="Choose image"]
    Click Element   xpath://*[text()="Choose image"]

    Wait Until Page Contains Element    xpath://*[text()="0"] 
    Click Element   xpath://*[text()="0"]
    
    Wait Until Page Contains Element     xpath://*[text()="Store images"]
    Click Element   xpath://*[text()="Store images"]


*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Test if page contains "Data" 
    Open Browser    about:blank    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}
    Go To           ${URL}

    Wait Until Page Contains     Data   20s
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

    Select Dataset
    Wait Until Page Contains    Upload images
    Wait Until Page Contains Element    xpath:(//section[@data-testid='stFileUploadDropzone']//input)[last()]
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
    Close Browser

Test image displaying

    Open Browser    about:blank    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}
    Go To           ${URL}

    Select dataset
    Wait Until Page Contains    Person Detection dataset
    Wait Until Page Contains    1/8

    Click Element        xpath://*[text()="Next"]
    Wait Until Page Contains    2/8

    Click Element        xpath://*[text()="Previous"]
    Wait Until Page Contains    1/8

    Close Browser

