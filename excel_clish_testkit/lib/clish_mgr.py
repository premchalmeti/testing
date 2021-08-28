import subprocess

import constants
import utils


class ClishManager:
    """
    A class to run CLISH commands
    `CLISH_SCRIPT` points to actual CLISH executable

    >>> ClishManager().run("device add 10.221.44.251")

    """
    CLISH_SCRIPT = '/usr/bin/clish'
    USER = 'admin'

    def __init__(self):
        self.cmd = ""
        self.logger = utils.get_logger(f"{constants.CURRENT_TC}.{self.__class__.__name__}")

    def run(self, cmd, inputs=""):
        # todo: change to ssh and run on node and replace subprocess to pexpect
        self.cmd = cmd

        executable_cmd = self._get_clish_executable_cmd()

        self.logger.info(f"Running {executable_cmd}")
        self.logger.info(f"user: {self.USER}")
        self.logger.info(f"inputs: {inputs}")

        proc = subprocess.run(
            executable_cmd,
            input=inputs,
            shell=True,
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE,
            encoding='utf-8'
        )

        self.logger.info(f"{cmd} | stdout: {proc.stdout}, stderr: {proc.stderr}")

        return proc.stdout, proc.stderr

    def _get_clish_executable_cmd(self):
        return f'{self.CLISH_SCRIPT} -u {self.USER} -c "{self.cmd}"'
