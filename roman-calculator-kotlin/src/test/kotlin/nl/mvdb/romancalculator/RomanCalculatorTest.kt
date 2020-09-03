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
    fun testFlattenSubtractives() {
        val c = RomanCalculator()
        assertEquals("IIII", RomanNumber("IV").flattenSubtractives())
        assertEquals("VIIII", RomanNumber("IX").flattenSubtractives())
        assertEquals("XVIIII", RomanNumber("XIX").flattenSubtractives())
        assertEquals("MDCCCCXVIIII", RomanNumber("MCMXIX").flattenSubtractives())
    }

    @Test
    fun testInflateSubtractives() {
        val c = RomanCalculator()
        assertEquals("IV", RomanNumber("IIII").shorten())
        assertEquals("IX", RomanNumber("VIIII").shorten())
        assertEquals("XIX", RomanNumber("XVIIII").shorten())
        assertEquals("MCMXIX", RomanNumber("MDCCCCXVIIII").shorten())
    }
}