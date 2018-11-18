class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        Count0 = Count1 = Count2 = 0
        for i in nums:
            if i == 0:
                Count0 += 1
            elif i == 1:
                Count1 += 1
            else:
                Count2 += 1
        
        for index in range(0,len(nums)):
            if index < Count0:
                nums[index] = 0
            elif index < Count0 + Count1:
                nums[index] = 1
            else:
                nums[index] = 2
