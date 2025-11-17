fun main() {
    val c1 = readLine()!!
    val c2 = readLine()!!
    val c3 = readLine()!!

    val colors = listOf(
        "black", "brown", "red", "orange", "yellow",
        "green", "blue", "violet", "grey", "white"
    )

    val first = colors.indexOf(c1)      // 첫 번째 색의 값
    val second = colors.indexOf(c2)     // 두 번째 색의 값
    val multiplier = colors.indexOf(c3) // 세 번째 색의 제곱

    val value = (first * 10 + second) * Math.pow(10.0, multiplier.toDouble()).toLong()

    println(value)
}
