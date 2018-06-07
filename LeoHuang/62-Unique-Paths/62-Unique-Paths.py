class Solution(object):
  def uniquePaths(self, m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    maxValue = m if m > n else n
    minValue = m + n - maxValue
    numerator = m + n
    numeratorFactorial = list(range(numerator - minValue, numerator))
    denpminatorFactorial = list(range(1, minValue))
    result = 1
    for i in range(len(denpminatorFactorial)):
      result = result * numeratorFactorial[i] / denpminatorFactorial[i]
    return result
