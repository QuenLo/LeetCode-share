class Solution(object):
  def maxDistToClosest(self, seats):
    """
    :type seats: List[int]
    :rtype: int
    """
    seatsStr = ''.join(str(num) for num in seats)
    maxDistance = 0
    for zeros in re.finditer(r'0+', seatsStr):
			# re.finditer returns start and end position of the string
			# doc: https://docs.python.org/2/library/re.html#finding-all-adverbs-and-their-positions
      zero = zeros.group(0)
      if zeros.start() == 0:
        maxDistance = len(zero)
      elif zeros.end() == len(seats):
        if maxDistance < len(zero):
          maxDistance = len(zero)
      elif maxDistance < int((len(zero) + 1) / 2):
        maxDistance = int((len(zero) + 1)/ 2)
    return maxDistance
