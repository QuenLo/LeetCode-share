# Problem
https://leetcode.com/problems/unique-paths/description/

# Scala - imperative
```
object Solution {
  def uniquePaths(m: Int, n: Int): Int = {
      choose(m + n - 2, n - 1)
  }
  def choose(n: Int, k: Int) = {
    if (k > n) 0
    else {
      var accumulator: BigInt = 1
      var fac: Int = n
      for (iter <- 1 to n - k) {
        accumulator = accumulator * fac
        fac = fac - 1
        accumulator = accumulator / iter
      }
      accumulator.toInt
    }
  }
    
}
```

# Comment
Use BigInt instead of Long as accumulator