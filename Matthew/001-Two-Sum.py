class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = 0
        while(n != len(nums)):
            z = target - nums[n]
            try:
                return n, nums.index(z, n+1)
            except:pass
            n += 1
