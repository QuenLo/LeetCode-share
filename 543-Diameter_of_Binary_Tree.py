# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        maxi = 0
        
        def dfs( node ):
            nonlocal maxi
            
            if node is None:
                return -1
            
            left = dfs( node.left ) + 1
            right = dfs( node.right ) + 1
            
            cur_sum = left + right
            maxi = max( cur_sum, maxi )
            
            return max( left, right )
        
        dfs( root )
        return maxi
