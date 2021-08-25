# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        All_set = set()
        return self.findnum( All_set, root, k )
    
    def findnum( self, All_set, cur, k ):
        if cur is None:
            return False
        if k-cur.val in All_set:
            return True
        All_set.add(cur.val)
        return self.findnum( All_set, cur.right, k ) or self.findnum( All_set, cur.left, k )
