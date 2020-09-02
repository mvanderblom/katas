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
}