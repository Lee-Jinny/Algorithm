import java.io.BufferedReader
import java.io.InputStreamReader

fun main() {
    // 입력
    val br = BufferedReader(InputStreamReader(System.`in`))

    while (true) {
        val line = br.readLine() ?: break  // 한 줄 읽기
        val parts = line.split(" ") // 공백 기준 분리 후 리스트에 담기

        val name = parts[0]
        val age = parts[1].toInt()
        val weight = parts[2].toInt()
        
        // 종료조건
        if (name == "#" && age == 0 && weight == 0) {
            break
        }
        
        // 시니어 주니어 구분
        if (age > 17 || weight >= 80 ) {
            println("$name Senior")
        } else {
            println("$name Junior")
        }
        
    }
}