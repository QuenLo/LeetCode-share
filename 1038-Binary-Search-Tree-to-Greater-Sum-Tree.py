# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    ListNode = []
    def bstToGst(self, root):
        self.ListNode = []
        self.dfs( root )
        SumNum = 0

        for node in self.ListNode:
            SumNum += node.val
            node.val = SumNum
        return root
    
    def dfs(self, node):
        if node:
            if node.right:
                self.dfs( node.right )
            self.ListNode.append( node )
            if node.left:
                self.dfs( node.left )
                
class SolutionII(object):
    def bstToGst(self, root):
        self.bstToGst2( root, 0 )
        return root
    
    def bstToGst2( self, root, SumNum ):
        if root.right:
            SumNum = self.bstToGst2( root.right, SumNum )
        root.val += SumNum
        SumNum = root.val
        if root.left:
            SumNum = self.bstToGst2( root.left, SumNum )
        return SumNum
        
        
class SolutionIII(object):
    val = 0
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root.right:
            self.bstToGst( root.right )
        root.val += self.val
        self.val = root.val
        if root.left:
            self.bstToGst(root.left)
        return root
