# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        
        if not root:
            return None
        
        if root.val < key:
            root.right = self.deleteNode( root.right, key )
        elif root.val > key:
            root.left = self.deleteNode( root.left, key )
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            else:
                root.val = self.findMax( root.left )
                root.left = self.deleteNode( root.left, root.val )
        
        return root
    
    def findMax( self, root ):
        if not root:
            return None
        else:
            while root.right:
                root = root.right
            return root.val
        
