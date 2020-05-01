# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

### Runtime: 96 ms ###
class Solution1:
    ans = -2**32
    
    def maxPathSum(self, root: TreeNode) -> int: 
        self.countUnit(root)
        return self.ans
        
    def countUnit(self, root: TreeNode) -> int:

        if root is None:
            return 0

        lsum = max( 0, self.countUnit( root.left) )
        rsum = max( 0, self.countUnit( root.right) )

        self.ans = max( self.ans, root.val+lsum+rsum )
        
        return max(lsum,rsum) + root.val


### Runtime: 88 ms ###
class Solution2:
    ans = 0
    
    def maxPathSum(self, root: TreeNode) -> int: 
        self.countUnit(root)
        return self.ans
        
    def countUnit(self, root: TreeNode) -> int:

        if root is None:
            return 0

        lsum = max( 0, self.countUnit( root.left) )
        rsum = max( 0, self.countUnit( root.right) )

        # ans have value
        if self.ans:
            self.ans = max( self.ans, root.val+lsum+rsum )
        else:
            self.ans = root.val+lsum+rsum
            
        return max(lsum,rsum) + root.val
