# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## Iterative Solution
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        node = root
        while node:
            
            if node.left:
                
                # find the mostright
                mostright = node.left
                while mostright.right:
                    mostright = mostright.right
                
                # connect mostright to right
                mostright.right = node.right
                node.right = node.left
                node.left = None
                
            node = node.right


class SolutionI:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        # pre-order
        order = []
        def dfs( node ):
            
            if not node:
                return
            
            order.append( node.val )
            dfs( node.left )
            dfs( node.right )
        
        dfs(root)
        print(order)
        
        for o in order[:-1]:
            root.val = o
            root.left = None
            root.right = TreeNode()
            root = root.right
        
        root.val = order[-1]
        root.right = None
        root.left = None
            
            
