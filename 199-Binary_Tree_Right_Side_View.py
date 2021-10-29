# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        row_collection = collections.defaultdict(list)
        
        def dfs( node, col, row ):
            
            if not node:
                return
            
            row_collection[row].append( [ col, node.val ] )
            dfs( node.left, col-1, row+1 )
            dfs( node.right, col+1, row+1 )
            
            
        output = []
        dfs( root, 0, 0 )
    
        row_collection = dict(sorted( row_collection.items() ))
        for row in row_collection:
            output.append( row_collection[row][-1][1] )
            
        return output
