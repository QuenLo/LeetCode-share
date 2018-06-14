# Problem
https://leetcode.com/problems/sqrtx/description/

# Scala
```
object Solution {
  def mySqrt(x: Int): Int = {
    Math.floor(iter(1, x)).toInt
  }
  
  def iter(current: Double, target: Int): Double = {
    if (isValid(current, target)) current
    else iter(current - functionValue(target)(current) / derivative(current), target)
  }
  
  def isValid(x: Double, target: Int) = {
    Math.abs(x * x - target.toDouble) < 0.1
  }
  
  def functionValue(n: Int)(x: Double) = {
    x * x - n.toDouble
  }
  
  def derivative(x: Double): Double = {
    2 * x
  }
}
```