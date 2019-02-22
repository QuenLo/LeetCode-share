# python3

class Solution:
    def jump(self, nums: 'List[int]') -> 'int':
        
        lennums = len(nums)

        step, end, start, maxend = 0, 0, 0, 0
        
        while end < lennums - 1 :
            step += 1
            maxend = end + 1
            
            for i in range(start, end+1):
                maxend = max( maxend, i + nums[i] )
            
            end, start = maxend, end + 1
            
        return step
