from typing import List


class Argument:
    def __init__(self, identifier, help_text):
        self.identifier = identifier
        self.help_text = help_text

    def parse(self, value: str):
        pass

    def default(self):
        pass


class StringArgument(Argument):
    def parse(self, value: str):
        return value

    def default(self):
        return ''


class BooleanArgument(Argument):
    def parse(self, value: str):
        return True

    def default(self):
        return False


class IntegerArgument(Argument):
    def parse(self, value: str):
        return int(value)

    def default(self):
        return 0


class ListArgument(Argument):
    def __init__(self, identifier: str, help_text: str, parser):
        self.identifier = identifier
        self.help_text = help_text
        self._parser = parser

    def parse(self, value: str):
        return list(map(self._parser, value.split(',')))

    def default(self):
        return []


class Schema:
    def __init__(self, arguments: List[Argument]):
        self.args_by_identifier = {arg.identifier: arg for arg in arguments}

    def __getitem__(self, item):
        return self.args_by_identifier[item]

    def __iter__(self):
        self.args_by_identifier.items().__iter__()

    def get_help_text(self):
        help_texts = ["Command usage: "]
        for arg in self.args_by_identifier.values():
            type_string = f"({str(arg.__class__.__name__).replace('Argument', '').lower()})"
            help_texts.append(f"\t-{arg.identifier}\t{type_string.ljust(9, ' ')}\t{arg.help_text}")
        return '\n'.join(help_texts)

    def __eq__(self, other):
        return self.args_by_identifier == other.args_by_identifier
