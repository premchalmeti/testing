
def device_delete(testcase, clish, operands, **kwargs):
    # setup function for device delete
    testcase.logger.info("Setting up device_delete() test", operands)
    clish.run_master(f"device add {operands.get('device_ip')}")
