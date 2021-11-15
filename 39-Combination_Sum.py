class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []
        
        def dfs( need, curr, start ):
            
            if need == 0:
                result.append( list(curr) )
                return
            
            for idx, c in enumerate(candidates[start:]):
                if need >= c:
                    dfs( need-c, curr + [c], start+idx )
                
        dfs( target, [], 0 )
        return result


class Solution_backtrack:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []
        
        def backtr( need, curr, start ):
            
            if need == 0:
                result.append( list(curr) )
                return
                
            elif need < 0:
                return
            
            for idx, c in enumerate(candidates[start:]):
                curr.append(c)
                backtr( need-c, curr, start+idx )
                curr.pop()
                
        backtr( target, [], 0 )
        return result
