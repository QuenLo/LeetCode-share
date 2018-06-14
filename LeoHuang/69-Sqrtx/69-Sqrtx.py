class Solution(object):
  def mySqrt(self, x):
    """
    :type x: int
    :rtype: int
		"""
    # newton's method: https://en.wikipedia.org/wiki/Newton%27s_method
    def newton(a, x): 
      # f(a) = a ^ 2 - x
      fA = a * a - x
      if(abs(fA) < 1):
        return a
      # b = y - ma
      b = fA - (2 * a) * a
      return newton(-1 * b / (2 * a), x)
    return int(newton(1.0, x))
