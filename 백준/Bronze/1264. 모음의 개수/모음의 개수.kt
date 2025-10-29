import java.io.BufferedReader
import java.io.InputStreamReader

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val vowels = setOf('a','e','i','o','u')

    while (true) {
        val line = br.readLine() ?: break
        if (line == "#") break

        val cnt = line.lowercase().count { it in vowels }
        println(cnt)
    }
}