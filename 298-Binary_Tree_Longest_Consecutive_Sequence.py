# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        
        def dfs( need, node, cur ):
            
            if node is None:
                return cur
            
            if node.val != need:
                left = dfs( node.val+1, node.left, 1 )
                right = dfs( node.val+1, node.right, 1 )
                return max( [ left, right, cur ] )
            
            left = dfs( node.val+1, node.left, cur+1 )
            right = dfs( node.val+1, node.right, cur+1 )
            return max( left, right )
                
        return max( dfs( root.val+1, root.left, 1 ), dfs( root.val+1, root.right, 1 ) )
