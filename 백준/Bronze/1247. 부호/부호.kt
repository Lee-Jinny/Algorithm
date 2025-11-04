import java.math.BigInteger

fun main() {
    // 테스트 셋 3개
    repeat(3) {
        val n = readLine()!!.toInt()

        // 큰 수의 합을 저장하기 위해서 & 초기 합 0
        var sum = BigInteger.ZERO

        // 처음 입력받은 n 만큼 반복하면서 sum 을 구하기
        repeat(n) {
            val num = readLine()!!.toBigInteger()
            sum += num
        }

        // 부호에 따라서 케이스를 나눔
        when {
            sum > BigInteger.ZERO -> println("+")
            sum < BigInteger.ZERO -> println("-")
            else -> println("0")
        }
    }
}