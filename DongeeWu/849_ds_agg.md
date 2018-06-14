# Problem
https://leetcode.com/problems/maximize-distance-to-closest-person/description/

# Scala - tail recursion
```
object Solution {
    def maxDistToClosest(seats: Array[Int]): Int = {
      List(consecutiveZeros(seats, 0, 0), seats.indexOf(1), seats.reverse.indexOf(1)).max
    }
  
    def consecutiveZeros(seatLeft: Array[Int], currAcc: Int, currMax: Int): Int = {
      if (seatLeft.isEmpty) Math.ceil(currMax.toDouble / 2).toInt
      else if (seatLeft.head == 1) consecutiveZeros(seatLeft.tail, 0, currMax)
      else {
        val acc = currAcc + 1
        if (acc > currMax) consecutiveZeros(seatLeft.tail, acc, acc)
        else consecutiveZeros(seatLeft.tail, acc, currMax)
      }
    }
}
```