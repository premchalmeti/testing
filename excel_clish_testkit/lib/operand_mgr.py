import os
import yaml

import exceptions
import utils
import config
import constants


class OperandManager:
    """
    This class is used by command to read operands from operand files.
    Does the following,
    - read `config.CURRENT_TC`.yml file in `config.OPERANDS_DIR` location
    - takes cmd as argument
    - do a lookup operand lookup
    - return complete cmd to Command
    """
    def __init__(self, plain_cmd):
        self.logger = utils.get_logger(f"{constants.CURRENT_TC}.{self.__class__.__name__}")
        self.plain_cmd = plain_cmd
        self.all_cmd_operands = {}
        self.cmd_operands = {}
        self.operands_file_exists = None
        self.parse_operand_file()
        self.get_cmd_operands()

    def parse_operand_file(self):
        operand_file = os.path.join(config.OPERANDS_DIR, f'{constants.CURRENT_TC}.yml')
        self.logger.info(f"{self.plain_cmd} | Parsing {operand_file} operand file")

        try:
            with open(operand_file) as fd:
                self.all_cmd_operands = yaml.safe_load(fd)

            if not self.all_cmd_operands:
                raise yaml.YAMLError(f"Invalid {operand_file} file")

            self.operands_file_exists = True
        except FileNotFoundError:
            self.operands_file_exists = False
            self.logger.warning("Operand File not found", exc_info=True)
        except yaml.YAMLError as exc:
            self.logger.critical("Invalid YAML File", exc_info=True)
            raise exceptions.SkipTestError() from exc

    def get_cmd_operands(self):
        self.cmd_operands = self.all_cmd_operands.get(self.plain_cmd, {})

        if not self.cmd_operands:
            self.logger.warning(f"{self.plain_cmd} | operand specification not found")

    def get_operand(self, operand):
        param_name = utils.get_param(operand)
        self.logger.debug(f"{self.plain_cmd} | operand={operand} plain_operand={param_name}")

        param_val = self.cmd_operands.get(param_name, '')
        self.logger.info(f"{self.plain_cmd} | param={param_name} value={param_val}")

        if not utils.is_optional_param(operand) and (not self.operands_file_exists or not param_val):
            raise ValueError(f"Cmd {self.plain_cmd}: {operand} is required argument")

        return param_val

    def get_operands(self):
        return self.cmd_operands
