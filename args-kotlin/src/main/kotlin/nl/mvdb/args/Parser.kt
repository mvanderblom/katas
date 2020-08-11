package nl.mvdb.args

import java.lang.Exception

class Parser(private val schema: Schema) {

    private val ARG_REGEX = "-[a-zA-Z]".toRegex()

    fun parse(args: String)= parse(args.split(" "))

    fun parse(args: List<String>) = args.withIndex()
            .filter { (_, arg) -> ARG_REGEX.matches(arg) }
            .map { (index, arg) ->this.parseArg(arg[1].toString(), getArgValue(args, index)) }

    private fun getArgValue(args: List<String>, index: Int): String? =
        if (args.size > index + 1)  args.get(index + 1) else null


    private fun parseArg(identifier: String, value: String?): ParsedArgument {
        val argument = schema.get(identifier)

        try {
            return ParsedArgument(argument, argument.parse(value))
        } catch (e: Exception) {
            throw InvalidArgumentValueException(identifier, value)
        }
    }

}

data class ParsedArgument(val argument: AbstractArgument<out Any>, val parse: Any)
