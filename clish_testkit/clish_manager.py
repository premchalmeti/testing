

__author__ = 'premchalmeti'


class ClishManager:
    """
    A class to run CLISH commands
    `CLISH_BIN` points to actual CLISH executable
    `USER` is the CLISH user to under which commands are executed

    >>> ClishManager().run("router ip set 3.4.22.122")

    """
    CLISH_BIN = '/opt/clish/bin/clish'
    USER = 'admin'

    def get_complete_cmd(self):
        return f'{self.CLISH_BIN} -u {self.USER} -c "{self.cmd}"'

    def get_clish_output(self):
        import subprocess

        proc = subprocess.Popen(
            self.get_complete_cmd(),
            shell=True,
            stderr=subprocess.PIPE, stdout=subprocess.PIPE
        )

        stdout, stderr = proc.communicate()

        return stdout, stderr

    def run(self, cmd):
        self.cmd = cmd
        return self.get_clish_output()
