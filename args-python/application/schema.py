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


class BooleanArgument(StringArgument):
    def parse(self, value: str):
        return True

    def default(self):
        return False


class IntegerArgument(StringArgument):
    def parse(self, value: str):
        return int(value)

    def default(self):
        return 0


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
            help_texts.append(f"\t-{arg.identifier}\t({str(arg.__class__.__name__).replace('Argument', '').lower()})\t{arg.help_text}")
        return '\n'.join(help_texts)

    def __eq__(self, other):
        return self.args_by_identifier == other.args_by_identifier
