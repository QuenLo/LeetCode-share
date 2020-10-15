# Using Extra Array
class Solution1_1:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        Length = len(nums)
        k = k % Length
        
        temp = nums[-k:] + nums[0:-k]
        nums[:] = temp
        
class Solution1_2:
    def rotate(self, nums: List[int], k: int) -> None:
        Length = len(nums)
        k = k % Length
        
        temp = [0]*Length
        for i in range(Length):
            temp[ (i+k)%Length ] = nums[i]
        nums[:] = temp
        
# Brute Force (Time Limit)
class Solution2:
    def rotate(self, nums: List[int], k: int) -> None:
        Length = len(nums)
        k = k % Length
        
        for i in range(k):
            previous = nums[-1]
            for j in range(Length):
                nums[j], previous = previous, nums[j]
                
# Using Cyclic Replacements
class Solution3:
    def rotate(self, nums: List[int], k: int) -> None:
        Length = len(nums)
        k = k % Length
        
        start, count = 0, 0
        while count < Length:
            current, previous = start, nums[start]
            
            while True:
                index_x = (current + k) % Length
                nums[index_x], previous = previous, nums[index_x]
                current = index_x
                count += 1
                
                
# Using Reverse
class Solution4:
    def reverse(self, nums: List[int], start: int, end: int) -> None:
        while start < end:
            nums[end], nums[start] = nums[start], nums[end]
            start += 1
            end -= 1
    
    def rotate(self, nums: List[int], k: int) -> None:
        Length = len(nums)
        k = k%Length
        
        self.reverse( nums, 0,  Length-1)
        self.reverse( nums, 0, k-1 )
        self.reverse( nums, k, Length-1 )
                
                if start == current:
                    break
                
            start += 1
