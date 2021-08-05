# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        
        def DFS( NowNode, NowSum, ansL ):

            if NowNode is None: return None
            NowSum -= NowNode.val
            ansL.append( NowNode.val )

            if not NowNode.left and not NowNode.right and NowSum == 0:
                ansLs.append( ansL.copy() )
            else:
                DFS( NowNode.left, NowSum, ansL )
                DFS( NowNode.right, NowSum, ansL )
            
            ansL.pop()

        ansLs = []
        DFS( root, targetSum, [] )
        return ansLs
