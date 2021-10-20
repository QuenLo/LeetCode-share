# Time: O(NK)
class Solution:
    def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
        
        for _ in range(volume):
            cur = k
            
            # Left
            for index_l in range(k)[::-1]:
                if heights[index_l] < heights[index_l+1]: cur = index_l
                elif heights[index_l] > heights[index_l+1]: break
                        
            if cur < k:
                heights[cur] += 1
                continue
            
            #right
            for index_r in range( k+1, len(heights) ):
                if heights[index_r] < heights[index_r-1]: cur = index_r
                elif heights[index_r] > heights[index_r-1]: break
            
            heights[cur] += 1
        
        return heights
 
# Time: O(N+K)
class SolutionII:
    def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
        
        left, right = [], []
        left_lo = right_lo = k
        heights_len = len(heights)
        
        for _ in range(volume):
            
            while left_lo > 0 and heights[left_lo-1] <= heights[left_lo]:
                if heights[left_lo-1] < heights[left_lo]: left.append(left_lo-1)
                left_lo -= 1
                
            while right_lo+1 < heights_len and heights[right_lo+1] <= heights[right_lo]:
                if heights[right_lo+1] < heights[right_lo]: right.append(right_lo+1)
                right_lo += 1
            
            if left:
                index_l = left[-1]
                heights[index_l] += 1
                # not less 
                if heights[index_l] == heights[index_l+1]: left.pop()
                # equal -> less
                if left_lo <= index_l-1: left.append(index_l-1)
                continue
            
            if right:
                index_r = right[-1]
                heights[index_r] += 1
                # not less
                if heights[index_r] == heights[index_r-1]: right.pop()
                # equal -> less
                if right_lo >= index_r+1: right.append(index_r+1)
                continue
                
            # all heigher or equal
            heights[k] += 1
            if k>0 and heights[k-1] < heights[k]: left.append(k-1)
            if k+1 < heights_len and heights[k+1] < heights[k]: right.append(k+1)
        
        return  heights
    
