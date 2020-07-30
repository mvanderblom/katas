from unittest import TestCase

from application.schema import StringArgument, BooleanArgument, IntegerArgument, Schema
from application.exceptions import UnknownArgumentException, InvalidArgumentValueException
from application.parser import Parser, ParsedArguments


class TestParser(TestCase):
    def setUp(self) -> None:
        self.parser = Parser(Schema([
            BooleanArgument('l', 'Turns on logging'),
            IntegerArgument('p', 'Specifies Port'),
            StringArgument('d', 'Specifies Data dir')
        ]))

    def test_parse_converts_input(self):
        output_of_string = self.parser.parse('-l -p 8080 -d /usr/logs')
        output_of_list = self.parser.parse(['-l', '-p', '8080', '-d', '/usr/logs'])
        self.assertTrue(isinstance(output_of_string,  ParsedArguments))
        self.assertEqual(output_of_list, output_of_string)

    def test_novalue_arg_at_the_end_works(self):
        self.parser.parse('-l')

    def test_unknown_argument_fails(self):
        with self.assertRaises(UnknownArgumentException):
            self.parser.parse('-x')

    def test_argument_with_negative_int_value(self):
        self.parser.parse('-p -1')

    def test_argument_value_types(self):
        parsed_args = self.parser.parse('-l -p 8080 -d /usr/logs')
        self.assertTrue(isinstance(parsed_args['l'], bool))
        self.assertTrue(isinstance(parsed_args['p'], int))
        self.assertTrue(isinstance(parsed_args['d'], str))

    def test_invalid_value_for_argument_type_fails(self):
        with self.assertRaises(InvalidArgumentValueException):
            self.parser.parse('-p SomeString')

    def test_default_values(self):
        parsed_args = self.parser.parse('')
        self.assertEqual(False, parsed_args['l'])
        self.assertEqual(0, parsed_args['p'])
        self.assertEqual('', parsed_args['d'])
