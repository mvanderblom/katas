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
        return terms.joinToString("", transform = RomanNumber::spread)
                .toList().sorted()
                .joinToString ("")
                .toRoman()
                .shorten()

    }
}

data class RomanNumber(val number: String){
    private val subtractives = mapOf(
            "IV" to "IIII",
            "IX" to "VIIII",
            "XL" to "XXXX",
            "XC" to "VXXXX",
            "CD" to "CCCC",
            "CM" to "DCCCC"
    )

    private val synonims = mapOf(
            "IIIII" to "V",
            "VVVVVVVVVV" to "L",
            "LL" to "C",
            "CCCCC" to "D",
            "DD" to "M",
            "VIV" to "IX",
            "VXV" to "XC",
            "DCD" to "CM"
    )

    fun spread(): String {
        var flattenedNumber = number
        for ((short, long) in subtractives.entries)
            flattenedNumber = flattenedNumber.replace(short, long)

        return flattenedNumber
    }

    fun shorten(): String {
        var shortenedNumber = number

        for ((long, short) in synonims.entries)
            shortenedNumber = shortenedNumber.replace(long, short)

        for ((short, long) in subtractives.entries)
            shortenedNumber = shortenedNumber.replace(long, short)

        return shortenedNumber
    }
}

fun String.toRoman(): RomanNumber {
    return RomanNumber(this)
}