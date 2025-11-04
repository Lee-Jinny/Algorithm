import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.min

fun main(){
    val br = BufferedReader(InputStreamReader(System.`in`))

    while (true) {
        val line = br.readLine() ?: break  // 한 줄 읽기
        val parts = line.split(" ") // 공백 기준 분리

        val x = parts[0].toInt()
        val y = parts[1].toInt()
        val w = parts[2].toInt()
        val h = parts[3].toInt()

        // x축 최단거리
        val shortestX = min(x, w-x)

        // y축 최단거리
        val shortestY = min(y, h-y)

        val shortest = min(shortestX, shortestY)

        println(shortest)
    }
}