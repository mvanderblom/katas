package nl.mvdb.args

import java.lang.RuntimeException

open class ParserException(message: String) : RuntimeException(message)

class UnknownIdentifierException(identifier: String) : ParserException("Unknown argument provided: $identifier")

class InvalidArgumentValueException(identifier: String, value: String?) : ParserException("Invalid argument value provided: $identifier $value")
