# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def dfs( self, node, curtotal ):
            
        if not node :
            return curtotal

        node.val = node.val + self.dfs( node.right, curtotal )

        return self.dfs( node.left, node.val )
        
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        self.dfs(root, 0)
        
        return root
