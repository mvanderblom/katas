package nl.mvdb.greed

import org.junit.Assert.*
import org.junit.Test

class GreedTest() {
    private val greed = Greed()

    @Test
    fun testSingleOne() = assertEquals(100, greed.score(listOf(1)))

    @Test
    fun testSingleFive()= assertEquals(50, greed.score(listOf(5)))

    @Test
    fun testTripleOnes()= assertEquals(1000, greed.score(listOf(1, 1, 1)))

    @Test
    fun testTripleTwos()= assertEquals(200, greed.score(listOf(2, 2, 2)))

    @Test
    fun testTripleThrees()= assertEquals(300, greed.score(listOf(3, 3, 3)))

    @Test
    fun testTripleFours()= assertEquals(400, greed.score(listOf(4, 4, 4)))

    @Test
    fun testTripleFives()= assertEquals(500, greed.score(listOf(5, 5, 5)))

    @Test
    fun testTripleSixes()= assertEquals(600, greed.score(listOf(6, 6, 6)))

    @Test
    fun testFourOfAKind()= assertEquals(2000, greed.score(listOf(1, 1, 1, 1)))

    @Test
    fun testFiveOfAKind()= assertEquals(4000, greed.score(listOf(1, 1, 1, 1, 1)))

    @Test
    fun testSixOfAKind()= assertEquals(8000, greed.score(listOf(1, 1, 1, 1, 1, 1)))

    @Test
    fun testThreePairs()= assertEquals(800, greed.score(listOf(1, 1, 2, 2, 3, 3)))

    @Test
    fun testStraight()= assertEquals(1200, greed.score(listOf(1, 2, 3, 4, 5, 6)))

    @Test
    fun testStraightOutOfOrder()= assertEquals(1200, greed.score(listOf(4, 5, 6, 1, 2, 3)))

    @Test(expected = IllegalArgumentException::class)
    fun testTooManyDice() = greed.score(listOf(1, 2, 3, 4, 5, 6, 7))

}