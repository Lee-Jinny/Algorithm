fun main() {
    val T = readLine()!!.toInt()

    repeat(T) {
        val (a,b) = readLine()!!.split(" ").map { it.toInt() }

        // 일의 자리만 제곱에 영향을 미침
        val base = a % 10

        val pattern = when (base) {
            0 -> listOf(10)
            1 -> listOf(1)
            2 -> listOf(2,4,8,6)
            3 -> listOf(3,9,7,1)
            4 -> listOf(4,6)
            5 -> listOf(5)
            6 -> listOf(6)
            7 -> listOf(7,9,3,1)
            8 -> listOf(8,4,2,6)
            9 -> listOf(9,1)
            else -> listOf()
        }

        // 패턴에서 b 번째 값 선택
        val result = pattern[(b-1) % pattern.size]

        println(result)
        
    }
}