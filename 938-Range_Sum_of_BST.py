# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def find( node ):
            
            if not node:
                return 0
                
            if node.val > high:
                return find(node.left)
            elif node.val < low:
                return find(node.right)
            else:
                return node.val + find(node.right) + find(node.left)
        
        return find(root)
