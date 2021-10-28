# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## BFS
# Time: O(NlogN)
from collections import defaultdict
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        col_table = defaultdict(list)
        queue = deque( [(root, 0)] )
        
        while queue:
            node, col = queue.popleft()
            
            if node is not None:
                col_table[ col ].append( node.val )
                
                queue.append( (node.left, col-1) )
                queue.append( (node.right, col+1) )
            
        return [ col_table[col] for col in sorted(col_table.keys()) ]

## DFS
# Time: O(W * HlogH), 
from collections import defaultdict
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ans_coll = defaultdict(list)
        left_col = right_col = 0
        
        def dfs( node, row, col ):
            nonlocal left_col, right_col
            
            if node is not None:
                ans_coll[col].append( (row, node.val) )
                left_col = min( left_col, col )
                right_col = max( right_col, col )
                
                dfs( node.left, row+1, col-1 )
                dfs( node.right, row+1, col+1 )
        
        if not root:
            return []
        dfs( root, 0, 0 )
        
        ans_array = []
        for col in range( left_col, right_col+1 ):
            # sort by row
            ans_coll[col].sort( key = lambda x: x[0] )
            temp = [ val[1] for val in ans_coll[col] ]
            ans_array.append(temp)
        
        return ans_array
