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
    fun testParseConvertsInput() {
        val outputOfString = parser.parse("-l -p 8080 -d /usr/logs")
        val outputOfList = parser.parse(listOf("-l", "-p", "8080", "-d", "/usr/logs"))
        assertEquals(outputOfString, outputOfList)
    }

    @Test
    fun testArgumentOrderDoesntMatter(){
        var output1 = parser.parse("-l -p 8080 -d /usr/logs")
        var output2 = parser.parse("-d /usr/logs -p 8080 -l")
        assertEquals(output1, output2)
    }

    @Test
    fun testNovalueArgAtTheEndWorks(){
        parser.parse("-l")
    }

    @Test(expected = UnknownIdentifierException::class)
    fun testUnknownArgumentThrows(){
        parser.parse("-x")
    }

    @Test
    fun testArgumentWithNegativeIntValue(){
        parser.parse("-p -1")
    }

    @Test
    fun testArgumentValueTypes(){
        val parsedArgs = parser.parse("-l -p 8080 -d /usr/logs -g 1,2,3,4,5,6 -s hello,world")
        assertTrue(parsedArgs["l"] is Boolean)
        assertTrue(parsedArgs["p"] is Int)
        assertTrue(parsedArgs["d"] is String)

        assertTrue(parsedArgs["g"] is List<*>)
        assertTrue((parsedArgs["g"] as List<*>).get(0) is Int)

        assertTrue(parsedArgs["s"] is List<*>)
        assertTrue((parsedArgs["s"] as List<*>).get(0) is String)
    }

    @Test(expected = InvalidArgumentValueException::class)
    fun testInvalidValueForArgumentTypeFails() {
        parser.parse("-p SomeString")
    }

    @Test
    fun testDefaultValues() {
        val parsedArgs = parser.parse("")
        assertEquals(false, parsedArgs["l"])
        assertEquals(0, parsedArgs["p"])
        assertEquals("", parsedArgs["d"])
        assertEquals(emptyList<Any>(), parsedArgs["g"])
        assertEquals(emptyList<Any>(), parsedArgs["s"])
    }

}
