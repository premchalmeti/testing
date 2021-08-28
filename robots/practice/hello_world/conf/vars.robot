*** Settings ***
Documentation       A list of variables


*** Variables ***
# argument and variable names are case-insensitive
# variables can be, 
# 1. scalar             ($ prefix: ${URL})
# 2. list               (@ prefix: @{results})
# 3. Dicotionaries      (& prefix)
# 4. environment        (% prefix)


${GOOGLE_URL}        https://google.co.in
${SEARCH_QUERY}     Hello world!
${BROWSER}          Firefox
