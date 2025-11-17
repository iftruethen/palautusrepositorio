*** Settings ***
Resource  resource.robot
Test Setup      Open And Configure Browser
Test Teardown   Close Browser

*** Test Cases ***
When counter has a nonzero value and it is reset the value becomes zero
    Go To    ${HOME_URL}
    Click Button    Paina
    Click Button    Paina

    Click Button    Nollaa
    Page Should Contain    nappia painettu 0 kertaa
