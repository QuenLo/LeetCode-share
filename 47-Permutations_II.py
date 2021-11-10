## Backtracking
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        count = collections.Counter(nums)
        len_nums = len(nums)
        
        result = []
        
        def back( cur, count ):
            nonlocal result
            if len(cur) == len_nums:
                result.append( list(cur) )
                return
            
            for c in count:
                if count[c] > 0:
                    cur.append( c )
                    count[c] -= 1
                    back( cur, count )
                    cur.pop()
                    count[c] += 1
                    
        back( [], count )
        return result
