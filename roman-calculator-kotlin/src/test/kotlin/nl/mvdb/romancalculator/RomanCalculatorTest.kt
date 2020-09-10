package nl.mvdb.romancalculator

import org.junit.Assert.assertEquals
import org.junit.Test

class RomanCalculatorTest {

    @Test
    fun testOnePlusOneShouldEqualTwo() {
        val calculator = RomanCalculator()
        calculator.enter("I")
        calculator.enter("I")
        assertEquals("II", calculator.add())
    }

    @Test
    fun testTwoPlusTwoShouldEqualFour() {
        val calculator = RomanCalculator()
        calculator.enter("II")
        calculator.enter("II")
        assertEquals("IV", calculator.add())
    }

    @Test
    fun testFourPlusFiveShouldEqualNine() {
        val calculator = RomanCalculator()
        calculator.enter("IV")
        calculator.enter("V")
        assertEquals("X", calculator.add())
    }

    @Test
    fun testSpread() {
        assertEquals("IIII", "IV".toRoman().spread())
        assertEquals("VIIII", "IX".toRoman().spread())
        assertEquals("XVIIII", "XIX".toRoman().spread())
        assertEquals("MDCCCCXVIIII", "MCMXIX".toRoman().spread())
    }

    @Test
    fun testShorten() {
        assertEquals("IV", "IIII".toRoman().shorten())
        assertEquals("IX", "VIIII".toRoman().shorten())
        assertEquals("XIX", "XVIIII".toRoman().shorten())
        assertEquals("MCMXIX", "MDCCCCXVIIII".toRoman().shorten())
    }

    @Test
    fun testShortenLengthySequences() {
        assertEquals("VI", "IIIIII".toRoman().shorten())
    }
}