package nl.mvdb.romancalculator

class RomanCalculator {
    private val input = mutableListOf<String>()

    fun enter(s: String) {
        input.add(s)
    }

    fun add(): String {
        return input.joinToString("");
    }

}