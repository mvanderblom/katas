package nl.mvdb.romancalculator

import java.lang.IllegalArgumentException

val ROMAN_NUMERALS = "IVXLCDM"

class RomanCalculator {
    private val terms = mutableListOf<RomanNumber>()

    fun enter(number: String) {
        val upperCaseNumber = number.toUpperCase()
        for (c in upperCaseNumber)
            if(!ROMAN_NUMERALS.contains(c))
                throw IllegalArgumentException("${number} is not a valid roman number")

        terms.add(RomanNumber(upperCaseNumber))
    }

    fun add(): String {
        val x = terms
            .map(RomanNumber::flattenSubtractives)

        return ""
    }
}

data class RomanNumber(val number: String){
    private val subtractives = mapOf(
            "IV" to "IIII",
            "IX" to "VIIII",
            "XL" to "XXXX",
            "XC" to "VXXXX",
            "CD" to "CCCC",
            "CM" to "DCCCC",

            "IX" to "VIV",
            "XC" to "VXV",
            "CM" to "DCD"
    )

    fun flattenSubtractives(): String {
        var flattenedNumber = number
        for ((subtractive, replacement) in subtractives.entries)
            flattenedNumber = flattenedNumber.replace(subtractive, replacement)

        return flattenedNumber
    }

    fun shorten(): String {
        var shortenedNumber = number

        for ((subtractive, replacement) in subtractives.entries)
            shortenedNumber = shortenedNumber.replace(replacement, subtractive)

        return shortenedNumber
    }
}