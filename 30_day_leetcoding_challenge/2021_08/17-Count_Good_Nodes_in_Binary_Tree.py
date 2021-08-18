# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



## Sol: DFS, recursive
# Time: O(N)
# Space: O(logN), worst O(N)
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def iamMax( root, nowM ):
            
            if root is None:
                return 0
            
            Yes = 0
            if root.val >= nowM:
                Yes = 1
                nowM = root.val
            
            return Yes + iamMax( root.left, nowM ) + iamMax( root.right, nowM )
        
        return iamMax( root, root.val )
      
      

## Sol: DFS, interative
# Time: O(N)
# Space: O(logN), worst O(N)
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        stack = [ (root, root.val) ]
        goodnode_num = 0
        
        while stack:
            node, nowMax = stack.pop()
            if nowMax <= node.val:
                goodnode_num += 1
                nowMax = node.val
                
                
            if node.left is not None:
                stack.append( (node.left, nowMax) )
            if node.right is not None:
                stack.append( (node.right, nowMax) )
                
        return goodnode_num
      
