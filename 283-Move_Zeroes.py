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
        
class SolutionII:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = 0
        for cur in range(len(nums)):
            if nums[cur]:
                temp = nums[i], nums[cur]
                nums[cur], nums[i] = temp
                i += 1
