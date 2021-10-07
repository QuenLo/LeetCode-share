class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)
        stack = []
        
        for i, v in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < v:
                index = stack.pop()
                ans[index] = i - index
            stack.append( i )
            
        return ans
