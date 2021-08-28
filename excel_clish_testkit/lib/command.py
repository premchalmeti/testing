import config
import exceptions
import constants
import utils
from operand_mgr import OperandManager
from excel_mgr import ExcelManager


class Command:
    """
    A Command class is the actual executable entity of test and does following things,
        - use `OperandManager` to get operands
        - Executes command using `ClishManager`
        - Return result to testcase for assertions
        # self.complete_cmd: device add <device_ip>:
        # self.plain_cmd: device add:
        # self.executable_cmd: device add 10.221.44.251:
    """
    def __init__(self, cmd_row):
        self.logger = utils.get_logger(f"{constants.CURRENT_TC}.{self.__class__.__name__}")
        self.complete_cmd = cmd_row
        self.complete_cmd_str = " ".join(self.complete_cmd)
        self.stdout = ""
        self.stderr = ""

        self.plain_cmd = ExcelManager.get_cmd(self.complete_cmd)
        self.plain_cmd_str = " ".join(self.plain_cmd)
        self.lookup_cmd_str = "_".join(self.plain_cmd)

        self.logger.debug(f"{self.complete_cmd_str} | Plain cmd: {self.plain_cmd_str}")

        self.operand_mgr = OperandManager(self.plain_cmd_str)
        self.clish = utils.get_clish_instance()
        self.logger.debug(f"{self.complete_cmd_str} | Using clish instance: {self.clish}")

        self.executable_cmd = []

    def prepare_executable_cmd(self):
        try:
            if not self.executable_cmd:
                self.executable_cmd = [self.operand_mgr.get_operand(c) if utils.is_param(c) else c for c in self.complete_cmd]
        except ValueError as exc:
            self.logger.error(f"{self.complete_cmd_str} operand error", exc_info=True)
            raise exceptions.SkipTestError() from exc

        self.logger.debug(f"{self.complete_cmd_str} | complete executable cmd: {self.executable_cmd}")

    @property
    def readonly(self):
        return not any([utils.is_param(c) and not utils.is_optional_param(c) for c in self.complete_cmd])

    def run(self, *args, **kwargs):
        self.prepare_executable_cmd()

        self.logger.info(f"{self.complete_cmd_str} | Running executable cmd: {self.executable_cmd}")
        cmd = " ".join(self.executable_cmd)

        if config.READ_ONLY_RUN and not self.readonly:
            raise exceptions.SkipTestError(f"{self.complete_cmd_str} | cmd not read only. READ_ONLY_RUN is set")

        self.stdout, self.stderr = self.clish.run(
            cmd,
            *args, **kwargs
        )
        return self.stdout, self.stderr

    @property
    def operands(self):
        return self.operand_mgr.get_operands()

    def is_error(self):
        if not self.stdout:
            return False
        elif isinstance(self.stdout, str) and any([k in self.stdout.lower() for k in constants.OUTPUT_ERROR_KEYWORDS]):
            return True
        elif isinstance(self.stdout, dict) and self.stdout.get("header", {}).get('status') != constants.SUCCESS_VAL:
            return True
        return False
