class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        c_len = len(candidates)
        def backcount( remain, curr, comb, result ):
            
            if remain == 0:
                result.append( list(comb) )
                return
            
            for next_curr in range( curr, c_len ):
                
                value = candidates[next_curr]
                if curr < next_curr and candidates[next_curr-1] == value:
                    continue
                if remain - value < 0:
                    break
                comb.append(value)
                backcount( remain - value, next_curr+1, comb, result )
                comb.pop()
                

        candidates.sort()
        comb, result = [], []
        backcount( target, 0, comb, result )
        return result
