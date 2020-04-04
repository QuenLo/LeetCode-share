class Solution1:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_0 = nums.count(0)
        while nums.count(0):
            nums.remove(0)
        nums.extend( [0]*num_0 )
        
        
class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        last_non = 0
        for i in range( len(nums) ):
            if nums[i] != 0:
                temp = nums[ last_non ]
                nums[ last_non ] = nums[ i ]
                nums[ i ] = temp
                last_non += 1
