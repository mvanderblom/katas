package nl.mvdb.args

class Schema {
    private var argumentsByIdentifier: Map<String, AbstractArgument<out Any>>

    constructor(arguments:List<AbstractArgument<out Any>>) {
        this.argumentsByIdentifier = arguments.map { it.identifier to it }.toMap()
    }

    fun get(identifier: String) = this.argumentsByIdentifier[identifier]
    fun getHelpText() = this.argumentsByIdentifier.values.map {
            val type_string = it.javaClass.simpleName.replace("Argument", "").padStart(9, ' ')
            "\t-${it.identifier}\t${type_string}\t${it.helpText}"
        }.joinToString(System.lineSeparator(), prefix = "Command usage: ${System.lineSeparator()}")
}

abstract class AbstractArgument<T>(val identifier: String, val helpText: String) {
    abstract fun parse(arg: String): T
    abstract fun default(): T
}

class StringArgument(identifier: String, helpText: String) : AbstractArgument<String>(identifier, helpText) {
    override fun parse(arg: String)= arg
    override fun default() = ""
}

class BooleanArgument(identifier: String, helpText: String) : AbstractArgument<Boolean>(identifier, helpText) {
    override fun parse(arg: String) = true
    override fun default() = false
}

class IntArgument(identifier: String, helpText: String) : AbstractArgument<Int>(identifier, helpText) {
    override fun parse(arg: String) = Integer.valueOf(arg)
    override fun default() = 0
}

class ListArgument<T>(identifier: String, helpText: String, val parser: (String) -> T) : AbstractArgument<List<T>>(identifier, helpText) {
    override fun parse(arg: String) = arg.split(',').map { parser(it) }
    override fun default() = emptyList<T>()
}