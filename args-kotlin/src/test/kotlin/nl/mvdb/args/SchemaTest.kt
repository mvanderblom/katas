package nl.mvdb.args

import org.junit.Assert
import org.junit.Test

class SchemaTest {
    @Test
    fun getHelpText() {
        val schema = Schema(
            listOf(
                BooleanArgument("l", "Turns on logging"),
                IntArgument("p", "Specifies Port"),
                StringArgument("d", "Specifies Data dir")
            )
        )

        val helpText = schema.getHelpText()
        println(helpText)
        val expectedText = listOf(
            "Command usage: ",
            "\t-l\t  Boolean\tTurns on logging",
            "\t-p\t      Int\tSpecifies Port",
            "\t-d\t   String\tSpecifies Data dir"
        ).joinToString(System.lineSeparator())
        Assert.assertEquals(expectedText, helpText)
    }
}