import unittest

from application.schema import Schema, BooleanArgument, IntegerArgument, StringArgument


class TestSchema(unittest.TestCase):
    def test_something(self):
        schema = Schema([
            BooleanArgument('l', 'Turns on logging'),
            IntegerArgument('p', 'Specifies Port'),
            StringArgument('d', 'Specifies Data dir')
        ])

        help_text = schema.get_help_text()
        self.assertEqual(help_text, """Command usage: 
\t-l\t(boolean)\tTurns on logging
\t-p\t(integer)\tSpecifies Port
\t-d\t(string) \tSpecifies Data dir""")

