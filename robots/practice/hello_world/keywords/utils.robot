*** Settings ***
Documentation       Utility Keywords


*** Keywords ***
Do Search
    # argument and variable names are case-insensitive
    [Arguments]     ${query}
    Input Text      css:input[title=Search]      ${Query}
    Press Keys       None    RETURN

    # todo: get search result web elements and check results should not be empty
    # https://www.blazemeter.com/blog/robot-framework-the-ultimate-guide-to-running-your-tests
