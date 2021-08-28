# define metadata, import external libraries and resources
*** Settings ***
Documentation   Open firefox browser and search hello world and wait
Library         SeleniumLibrary
Resource        ../conf/vars.robot
Resource        ../keywords/utils.robot
Suite Setup     Open Browser    ${GOOGLE_URL}     ${BROWSER}
Suite Teardown  Close All Browsers


# add test cases
*** Test Cases ***
Google Search
    [Tags]          google  search
    Do Search   ${search_query}
