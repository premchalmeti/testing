# Excel CLISH TestKit
## Intro
`Excel CLISH testKit` is an **Excel based CLISH testkit** framework. 
The test runner reads testcases (excels). Each testcase contains collection (rows) of tests. 

Each test (row) is a command with operands. (look into `tests/device.xlsx` for sample testcase structure)

The `device add <device_ip>` is a sample test defined in `tests/device.xlsx` test case

There are two types of operands,

1. Optional params: `[<device_ip>]`
    - Optional params are enclosed in square brackets
2. Required params: `<device_ip>`
    - Required params are enclosed in angular brackets
    

## How it works???

1. Define your testcases in `config.TEST_SRC_DIR` (tests/device.xlsx) directory
2. Specify test command operands [optional]

    - Command: `device add <device_ip>`
    - Operands file: `operands/device.yml`
        

                device add:
                    device_ip: 10.221.44.125

3. Define test setup and cleanup hooks [optional]

    - Command: `device delete`
    - Setup hook: `hooks/setup/device.py`
      

            def device_delete(testcase, clish, operands, **kwargs):
                # to delete a device we have to add it first
                # this hook will be called before `device delete` test

    - Command: `device delete`
    - Cleanup hook: `hooks/setup/device.py`
      

            def device_add(testcase, clish, operands, **kwargs):
                # We have to delete the device added by test in cleanup
                # this hook will be called after to perform cleanup `device add` test


4. Start Testrunner to start testing. This will update the test results and output in testcase.

        pip install -r requirements.txt [for the very first time]
        
        python test.py


## Testcase Structure:

    A sample device testcase will have following structure

    - tests/
        device.xlsx
        ...
    - operands/
        device.yml
        ...
    - hooks/
        setup/
            device.py
            ...
        cleanup/
            device.py
            ...
    - logs/
        device.log
        ...
    ...


## Inside source code:
1. `test_runner.py`

    Main entrypoint for framework has 2 interfaces, `run_all()` and `run(tcname)`
   
    - `run_all()` scans Excel testcases in `config.TEST_SRC_DIR` location which internally call `run(tcname)`
    - Uses with `ExcelManager` to parse TC excel
    - Prepare `TestCase` and run `TestCase().test()`
    - update TestCase results
2. `excel_mgr.py`

    Parse the `config.CURRENT_TC` excel file and is responsible for following things,
    - read currently running TC (`constants.CURRENT_TC`)
    - return test_rows to test_runner instance
    - executes tests
    - update test rows with results and update TC excel
3. `testcase.py`
   
    The `TestCase` class is represents the tests(rows) in the given excel TC.
    Does the following things,
    - The actual class which do the testcase assertions
    - The command is passed to `Command()` obj
    - call setup hook before test case run
    - test():
        - calls `Command().run()`
        - and `do_assertions()`
    - call cleanup hook after test case run
4. `command.py`
   
    A Command class is the actual executable entity of test
    - use `OperandManager` to get operands
    - Executes command using `ClishManager`
    - Return result to testcase for assertions
5. `operand_mgr.py`
   
    This class is used by command to read operands from operand files.
    Does the following,
    - read `config.CURRENT_TC`.yml file in `config.OPERANDS_DIR` location
    - takes cmd as argument
    - do a lookup operand lookup
    - return complete cmd to Command


## Important Locations:

|Path|Configuration variable|Default Value|
|----|----------------------|-----|
|Excel TC location|TEST_SRC_DIR|tests/|
|TC setup hooks|SETUP_HOOK|hooks/setup/|
|TC cleanup hook|CLEANUP_HOOK|hooks/cleanup/|
|TC operands|OPERANDS_DIR|/operands/|


## Features:
1. Supports mock run (`config.MOCK_RUN`), run read only cmds (`config.READ_ONLY_RUN`)
2. Add tests in excel testcase at any time
3. Specify operands in isolation in operands file
4. Perform test setup and cleanup via hooks
5. Skip any tests by adding `Skip` to a true (y, t, true, yes) value

Drop an email for any queries/enhancements on premkumarchalmeti@gmail.com
