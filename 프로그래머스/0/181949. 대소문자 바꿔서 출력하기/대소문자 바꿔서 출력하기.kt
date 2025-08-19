fun main(args: Array<String>) {
    val s1 = readLine()!!
    
    val result = s1.map {
        if (it.isUpperCase()) {
            it.lowercase()
        } else {
            it.uppercase()
        }
    }.joinToString("")
    println(result)
}