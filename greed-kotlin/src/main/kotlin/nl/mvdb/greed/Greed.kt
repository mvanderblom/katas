package nl.mvdb.greed

class Greed () {
    private val outcomesInOrder = listOf(
            StraightOutcome(),
            ThreePairsOutcome(),
            NOfAKindOutcome(6),
            NOfAKindOutcome(5),
            NOfAKindOutcome(4),
            TripleOutcome(6),
            TripleOutcome(5),
            TripleOutcome(4),
            TripleOutcome(3),
            TripleOutcome(2),
            TripleOutcome(1),
            SingleOutcome(5),
            SingleOutcome(1)
        )

    fun score(dice: List<Int>): Int {
        if(dice.size > 6)
            throw IllegalArgumentException("Max 6 dice allowed")

        val sorted_dice = dice.sorted()

        for(outcome in outcomesInOrder) {
            if (outcome.check(sorted_dice))
                return outcome.score(sorted_dice)
        }

        return 0;
    }
}