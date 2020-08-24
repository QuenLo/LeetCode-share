# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        if root.left == None and root.right == None:
            return 0
        else: return self.sumOfLeftLeaves_count( root )
        
    def sumOfLeftLeaves_count( self, root: TreeNode ) -> int:
        if root.left == None and root.right == None:
            return root.val
        if root.left != None and root.right == None:
            return self.sumOfLeftLeaves_count( root.left )
        if root.left == None and root.right != None:
            if root.right.left == None and root.right.right == None:
                return 0
            else:
                return self.sumOfLeftLeaves_count( root.right )
            return self.sumOfLeftLeaves_count( root.right )
        if root.left != None and root.right != None:
            if root.right.left == None and root.right.right == None:
                return self.sumOfLeftLeaves_count( root.left )
            else:
                return self.sumOfLeftLeaves_count( root.right ) + self.sumOfLeftLeaves_count( root.left )
        return 0
