# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
    
        def dp( root: TreeNode ) -> int:
            if root == None: return 0
            l_dp = dp( root.left )
            r_dp = dp( root.right )
            
            if l_dp == -1 or r_dp == -1 or abs(l_dp - r_dp) > 1 : return -1

            return max( l_dp, r_dp ) + 1
        
        return dp( root ) != -1
