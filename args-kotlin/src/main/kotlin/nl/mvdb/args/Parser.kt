package nl.mvdb.args

import java.lang.Exception

class Parser(private val schema: Schema) {

    private val ARG_REGEX = "-[a-zA-Z]".toRegex()

    fun parse(args: String)= parse(args.split(" "))

    fun parse(args: List<String>) = ParsedArguments(schema, args.withIndex()
            .filter { (_, arg) -> ARG_REGEX.matches(arg) }
            .map { (index, arg) ->this.parseArg(arg[1].toString(), getArgValue(args, index)) }
            .sortedBy { x -> x.argument.identifier  })


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

data class ParsedArgument(val argument: AbstractArgument<out Any>, val value: Any)
data class ParsedArguments(val schema: Schema, val arguments: List<ParsedArgument>) {
    operator fun get(s: String): Any = this.arguments
        .singleOrNull{ pa -> pa.argument.identifier == s }
        ?.let { pa -> pa.value }
        ?: schema.get(s).default()

}