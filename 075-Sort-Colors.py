class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        index0, index1, index2 = 0, 0, len(nums)-1
        
        while index1 <= index2:
            if nums[index1] == 0:
                nums[index0], nums[index1] = 0, nums[index0]
                index1 += 1
                index0 += 1
            elif nums[index1] == 2:
                nums[index2], nums[index1] = 2, nums[index2]
                #index1 += 1
                index2 -= 1
            else:
                index1 += 1
