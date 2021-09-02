class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        
        popping_list = nums.copy()
        
        leng = 1
        Max_leng = 0

        start = nums[0]
        nums[0] = -1
        popping_list.remove(start)
        
        while popping_list:
            if nums[start] == -1:
                Max_leng = max( Max_leng, leng )
                start = popping_list[0]
                nums[ nums.index( start ) ] = -1
                leng = 1
                popping_list.remove(start)
                continue
                
            if nums[start] != -1:
                popping_list.remove(nums[start])
                next_s = nums[start]
                nums[start] = -1
                start = next_s
                leng += 1
            
                        
        return max(Max_leng, leng)
