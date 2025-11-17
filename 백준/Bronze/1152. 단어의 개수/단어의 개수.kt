fun main() {
    val line = readLine()!!.trim()
    
    if (line.isEmpty()) {
        println(0)
    } else {
        val count = line.split(" ").size
        println(count)
    }
}