class Solution:
    def countElements(self, arr: List[int]) -> int:
        
        ans = 0
        arr_set = set( arr )
        for i in arr:
            if (i+1) in arr_set:
                ans += 1 
                
        return ans
