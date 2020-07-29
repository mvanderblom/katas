from unittest import TestCase

from application.parser import Parser, Argument, BooleanArgument


class Test(TestCase):
    def setUp(self) -> None:
        self.parser = Parser([
            BooleanArgument('l', 'Turns on logging'),
            Argument('p', 'Specifies Port'),
            Argument('d', 'Specifies Data dir')
        ])

    def test_parse_converts_input(self):
        output_of_string = self.parser.parse('-l -p 8080 -d /usr/logs')
        output_of_list = self.parser.parse(['-l', '-p', '8080', '-d', '/usr/logs'])
        self.assertTrue(isinstance(output_of_string,  list))
        self.assertEqual(output_of_list, output_of_string)

    def test_novalue_arg_at_the_end_works(self):
        self.parser.parse('-l')
