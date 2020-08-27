package nl.mvdb.greed

fun <T>  List<T>.groupCount() = this.groupingBy { it }.eachCount()
fun <A, B> Map<A, B>.swithKeyAndValue() = this.entries.associate{ (k,v)-> v to k}