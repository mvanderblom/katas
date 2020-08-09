package nl.mvdb.args

import org.junit.Assert
import org.junit.Test

class SchemaTest {

    @Test
    fun get() {
    }

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
        Assert.assertEquals("""Command usage: 
	-l	  Boolean	Turns on logging
	-p	      Int	Specifies Port
	-d	   String	Specifies Data dir""", helpText)
    }
}