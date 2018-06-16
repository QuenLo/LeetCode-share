class Solution(object):
  def canJump(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if len(nums) == 1:
      return True
    if nums[0] == 0:
      return False
    # find the max jump in nums
    maxNum = max(nums)
    # check 0s in nums
    # since only the 0s will block way to the end
    # we only check if 0s will block or not
    for i in range(nums.count(0)):
      index = nums.index(0)
      # if 0 is the last element in nums
      # then return
      if index == len(nums) - 1:
        return True
      j = 1
      jump = False
      # check if we can go across the 0
      while(j <= maxNum and index - j >= 0):
        if nums[index - j] > j:
          j += maxNum
          jump = True
        j += 1
      if jump is False:
        return False
      else:
        nums[index] = -1
    return True
