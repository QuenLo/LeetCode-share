# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        node_array = []
        
        def dfs( node, col, row ):
            
            if not node:
                return
            
            node_array.append( (col, row, node.val) )
            dfs( node.left, col-1, row + 1 )
            dfs( node.right, col+1, row + 1 )
            
        dfs( root, 0, 0 )
        node_array.sort()
        
        ans_dict = defaultdict(list)
        for col, row, value in node_array:
            ans_dict[col].append( value )
        
        return ans_dict.values()
