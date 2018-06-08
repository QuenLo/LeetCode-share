class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = 1
        output = []
        for z in range(len(nums)):
            output.append(n)
            n *= nums[z]
        n = 1
        for z in range(len(nums)-1, -1, -1):
            output[z] = output[z]*n
            n *= nums[z]
        return output
