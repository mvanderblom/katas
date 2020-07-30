import sys

from application.schema import Schema, BooleanArgument, IntegerArgument, StringArgument, ListArgument
from application.exceptions import ParserException
from application.parser import Parser

if __name__ == '__main__':
    schema = Schema([
        BooleanArgument('l', 'Turns on logging'),
        IntegerArgument('p', 'Specifies Port'),
        StringArgument('d', 'Specifies Data dir'),
        ListArgument('g', 'Specifies a list of integers', int),
        ListArgument('s', 'Specifies a list of strings', str)
    ])
    parser = Parser(schema)
    try:
        parsed_args = parser.parse(sys.argv)
        print(parsed_args)
    except ParserException as e:
        print(e)
        print(schema.get_help_text())

