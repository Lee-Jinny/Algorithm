fun main() {
    val n = readLine()!!.toInt()
    val calls = readLine()!!.split(" ").map { it.toInt() }

    var ySum = 0
    var mSum = 0

    for (time in calls) {
        ySum += ((time / 30) + 1) * 10   // 영식 요금제: 30초마다 10원
        mSum += ((time / 60) + 1) * 15   // 민식 요금제: 60초마다 15원
    }

    when {
        ySum < mSum -> println("Y $ySum")
        mSum < ySum -> println("M $mSum")
        else -> println("Y M $ySum")
    }
}