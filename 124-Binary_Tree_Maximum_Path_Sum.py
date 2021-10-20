# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Time: O(N)
# Space: O(H), H = tree High, to keep recursive stack
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        max_sum = float('-inf')
        def max_gain(node):
            nonlocal max_sum
            
            if not node:
                return 0
            
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            
            price_cur = node.val + left_gain + right_gain
            
            max_sum = max( max_sum, price_cur )
            
            return node.val + max( left_gain, right_gain )
        
        max_gain(root)
        
        return max_sum
      
      
class SolutionII:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        max_sum = root.val
        
        def dfs( node ):
            nonlocal max_sum
            
            if not node:
                return 0
            
            l = dfs( node.left )
            r = dfs( node.right )
            
            max_sum = max( max_sum, node.val, node.val+l+r, node.val+l, node.val+r )
            
            return max( node.val, node.val+l, node.val+r )
        
        dfs(root)
        
        return max_sum
