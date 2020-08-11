package nl.mvdb.args

import junit.framework.Assert.assertEquals
import junit.framework.Assert.assertTrue
import org.junit.Before
import org.junit.Test


internal class ParserTest {

    lateinit var parser: Parser

    @Before
    fun setUp() {
        this.parser = Parser(Schema(
            listOf(
            BooleanArgument("l", "Turns on logging"),
            IntArgument("p", "Specifies Port"),
            StringArgument("d", "Specifies Data dir"),
            ListArgument("g", "Specifies a list of integers", Integer::valueOf),
            ListArgument("s", "Specifies a list of strings", { x -> x})
            )))
    }

    @Test
    fun test_parse_converts_input() {
        val outputOfString = parser.parse("-l -p 8080 -d /usr/logs")
        val outputOfList = parser.parse(listOf("-l", "-p", "8080", "-d", "/usr/logs"))
        assertTrue(outputOfList is List)
        assertEquals(outputOfString, outputOfList)
    }

    @Test
    fun test_argument_order_doesnt_matter(){
        var output1 = parser.parse("-l -p 8080 -d /usr/logs")
        var output2 = parser.parse("-d /usr/logs -p 8080 -l")
        assertTrue(output1 is List)
        assertEquals(output1, output2)
    }
//
//    fun test_novalue_arg_at_the_end_works():
//    parser.parse("-l")
//
//    fun test_unknown_argument_fails():
//    with assertRaises(UnknownArgumentException):
//    parser.parse("-x")
//
//    fun test_argument_with_negative_int_value():
//    parser.parse("-p -1")
//
//    fun test_argument_value_types():
//    parsed_args = parser.parse("-l -p 8080 -d /usr/logs -g 1,2,3,4,5,6 -s hello,world")
//    assertTrue(isinstance(parsed_args["l"], bool))
//    assertTrue(isinstance(parsed_args["p"], int))
//    assertTrue(isinstance(parsed_args["d"], str))
//
//    assertTrue(isinstance(parsed_args["g"], list))
//    assertTrue(isinstance(parsed_args["g"][0], int))
//
//    assertTrue(isinstance(parsed_args["s"], list))
//    assertTrue(isinstance(parsed_args["s"][0], str))
//
//    fun test_invalid_value_for_argument_type_fails():
//    with self.assertRaises(InvalidArgumentValueException):
//    self.parser.parse("-p SomeString")
//
//    fun test_default_values():
//    parsed_args = self.parser.parse('')
//    self.assertEqual(False, parsed_args['l'])
//    self.assertEqual(0, parsed_args['p'])
//    self.assertEqual('', parsed_args['d'])
//    self.assertEqual([], parsed_args['g'])
//    self.assertEqual([], parsed_args['s'])

}