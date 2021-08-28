
def device_add(testcase, clish, operands, **kwargs):
    # cleanup function for device add
    testcase.logger.info("Cleaning up device_add() test", operands)
    clish.run_master(f"device delete {operands.get('device_ip')}")
