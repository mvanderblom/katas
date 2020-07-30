from unittest import TestCase

from application.schema import StringArgument, BooleanArgument, IntegerArgument, Schema, ListArgument
from application.exceptions import UnknownArgumentException, InvalidArgumentValueException
from application.parser import Parser, ParsedArguments


class TestParser(TestCase):
    def setUp(self) -> None:
        self.parser = Parser(Schema([
            BooleanArgument('l', 'Turns on logging'),
            IntegerArgument('p', 'Specifies Port'),
            StringArgument('d', 'Specifies Data dir'),
            ListArgument('g', 'Specifies a list of integers', int),
            ListArgument('s', 'Specifies a list of strings', str)
        ]))

    def test_parse_converts_input(self):
        output_of_string = self.parser.parse('-l -p 8080 -d /usr/logs')
        output_of_list = self.parser.parse(['-l', '-p', '8080', '-d', '/usr/logs'])
        self.assertTrue(isinstance(output_of_string,  ParsedArguments))
        self.assertEqual(output_of_list, output_of_string)

    def test_argument_order_doesnt_matter(self):
        output_1 = self.parser.parse('-l -p 8080 -d /usr/logs')
        output_2 = self.parser.parse('-d /usr/logs -p 8080 -l')
        self.assertTrue(isinstance(output_1, ParsedArguments))
        self.assertEqual(output_1, output_2)

    def test_novalue_arg_at_the_end_works(self):
        self.parser.parse('-l')

    def test_unknown_argument_fails(self):
        with self.assertRaises(UnknownArgumentException):
            self.parser.parse('-x')

    def test_argument_with_negative_int_value(self):
        self.parser.parse('-p -1')

    def test_argument_value_types(self):
        parsed_args = self.parser.parse('-l -p 8080 -d /usr/logs -g 1,2,3,4,5,6 -s hello,world')
        self.assertTrue(isinstance(parsed_args['l'], bool))
        self.assertTrue(isinstance(parsed_args['p'], int))
        self.assertTrue(isinstance(parsed_args['d'], str))

        self.assertTrue(isinstance(parsed_args['g'], list))
        self.assertTrue(isinstance(parsed_args['g'][0], int))

        self.assertTrue(isinstance(parsed_args['s'], list))
        self.assertTrue(isinstance(parsed_args['s'][0], str))

    def test_invalid_value_for_argument_type_fails(self):
        with self.assertRaises(InvalidArgumentValueException):
            self.parser.parse('-p SomeString')

    def test_default_values(self):
        parsed_args = self.parser.parse('')
        self.assertEqual(False, parsed_args['l'])
        self.assertEqual(0, parsed_args['p'])
        self.assertEqual('', parsed_args['d'])
        self.assertEqual([], parsed_args['g'])
        self.assertEqual([], parsed_args['s'])

