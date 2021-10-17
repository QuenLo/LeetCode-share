class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i, count = 0, 0
        while i < len(nums):
            if not nums[i]:
                nums.pop(i)
                count+=1
            else:
                i += 1
                
        nums.extend([0]*count)
