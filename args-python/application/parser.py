import re
from typing import List, Any, Dict

from application.schema import Schema, Argument
from application.exceptions import UnknownArgumentException, InvalidArgumentValueException


class ParsedArgument:
    def __init__(self, argument: Argument, value: Any):
        self.argument = argument
        self.value = value


class ParsedArguments:
    def __init__(self, schema: Schema):
        self.schema = schema
        self.parsedArguments: Dict[str, ParsedArgument] = {}

    def __getitem__(self, item: str):
        if item in self.parsedArguments:
            return self.parsedArguments[item].value
        return self.schema[item].default()

    def __eq__(self, other):
        return self.schema == other.schema and self.parsedArguments == other.parsedArguments

    def add(self, parsedArgument: ParsedArgument):
        self.parsedArguments[parsedArgument.argument.identifier] = parsedArgument


class Parser:
    def __init__(self, schema: Schema):
        self.schema = schema

    def parse(self, args) -> ParsedArguments:
        if type(args) is str:
            args = args.split(' ')
        self._parse_list(args)
        return ParsedArguments(self.schema)

    def _parse_list(self, args: List[str]) -> ParsedArguments:
        parsed_arguments = ParsedArguments(self.schema)
        for i, arg in enumerate(args):
            if re.match('-[a-zA-Z]', arg):
                parsed_argument = self._parse_arg(arg, self._get_arg_value(args, i))
                parsed_arguments.add(parsed_argument)
        return parsed_arguments

    def _parse_arg(self, arg: str, arg_value: str):
        try:
            argument = self.schema[arg[1]]
        except KeyError:
            raise UnknownArgumentException(arg)

        try:
            return ParsedArgument(argument, argument.parse(arg_value))
        except Exception:
            raise InvalidArgumentValueException(arg, arg_value)

    @staticmethod
    def _get_arg_value(args, i):
        try:
            arg_value = args[i + 1]
        except IndexError:
            arg_value = None
        return arg_value
