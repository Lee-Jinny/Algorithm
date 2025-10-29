import java.io.BufferedReader
import java.io.InputStreamReader

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val vowels = setOf('a','e','i','o','u')

    while (true) {
        val line = br.readLine()
        // 입력이 끝나면 종료
        if (line == null) {
            break
        }
        // # 이 나오면 종료
        if (line == "#") break
        
        // 소문자로 변경한 뒤 숫자 세기
        val cnt = line.lowercase().count { it in vowels }
        println(cnt)
    }
}