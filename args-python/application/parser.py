from typing import Dict, List


class Argument:
    def __init__(self, identifier, help_text):
        self.identifier = identifier
        self.help_text = help_text
        self.value = None

    def parse(self, value: str):
        pass

    def value(self):
        return self.value


class BooleanArgument(Argument):
    def parse(self, value: str):
        self.value = True


class Parser:
    def __init__(self, schema: List[Argument]):
        self.schema_by_identifier = {arg.identifier: arg for arg in schema}

    def parse(self, args) -> List[Argument]:
        if type(args) is str:
            args = args.split(' ')
        return self._parse_list(args)

    def _parse_list(self, args: List[str]) -> List[Argument]:
        print(args)

        for i, arg in enumerate(args):
            if arg[0] == '-':
                arg_value = self.get_arg_value(args, i)
                self.schema_by_identifier[arg[1]].parse(arg_value)

        return args

    def get_arg_value(self, args, i):
        try:
            arg_value = args[i + 1]
        except IndexError:
            arg_value = None
        return arg_value

