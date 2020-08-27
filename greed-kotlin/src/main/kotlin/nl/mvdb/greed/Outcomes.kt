package nl.mvdb.greed

interface Outcome {
    fun check(dice: List<Int>): Boolean
    fun score(dice: List<Int>): Int
}

abstract class NumberedOutcome(val number: Int) : Outcome

class StraightOutcome : Outcome {
    override fun check(dice: List<Int>) = dice == listOf(1, 2, 3, 4, 5, 6)
    override fun score(dice: List<Int>) = 1200
}

class SingleOutcome(number: Int) : NumberedOutcome(number) {
    override fun check(dice: List<Int>) = dice.contains(number)
    override fun score(dice: List<Int>) = when(number) {
        1 -> 100
        5 -> 50
        else -> 0
    }
}

class TripleOutcome(number: Int) : NumberedOutcome(number) {
    override fun check(dice: List<Int>) = dice.count { die -> die == number } == 3
    override fun score(dice: List<Int>) = when(number) {
        1 -> 1000
        else -> number * 100
    }
}

class ThreePairsOutcome : Outcome {
    override fun check(dice: List<Int>) = dice.groupCount().values
        .filter { count -> count == 2 }
        .count() == 3

    override fun score(dice: List<Int>) = 800
}

class NOfAKindOutcome(number: Int) : NumberedOutcome(number) {
    private val factors = mapOf(6 to 8, 5 to 4, 4 to 2)
    override fun check(dice: List<Int>) = dice.groupCount().values.contains(number)
    override fun score(dice: List<Int>): Int {
        val die = dice.groupCount()
            .swithKeyAndValue()
            .getValue(number)
        return TripleOutcome(die).score(dice) * factors.getValue(number)
    }
}