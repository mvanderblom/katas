import sys

from application.schema import Schema, BooleanArgument, IntegerArgument, StringArgument
from application.exceptions import ParserException
from application.parser import Parser

if __name__ == '__main__':
    schema = Schema([
        BooleanArgument('l', 'Turns on logging'),
        IntegerArgument('p', 'Specifies Port'),
        StringArgument('d', 'Specifies Data dir')
    ])
    parser = Parser(schema)
    try:
        parsed_args = parser.parse(sys.argv)

    except ParserException as e:
        print(e)
        print(schema.get_help_text())

