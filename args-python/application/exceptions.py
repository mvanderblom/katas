class ParserException(Exception):
    pass


class UnknownArgumentException(ParserException):
    def __init__(self, argument: str):
        self.argument = argument

    def __str__(self):
        return f"Unknown argument provided: {self.argument}"

class InvalidArgumentValueException(ParserException):
    def __init__(self, argument, value):
        self.argument = argument
        self.value = value

    def __str__(self):
        return f"Invalid argument value provided: {self.argument} {self.value}"
