# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## Sol: DFS
# Using recursion, keep track of depth and use it as index for the List List array.
## Time: O(N)
## Space: O(N)
class SolutionI:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if root is None: return []
        
        ansL = []
        ansL.append( [] )
        self.NextLevel( root, 0, ansL )
        
        return ansL
    
    def NextLevel( self, root, Level, ansL ):
        
        if root is None: return
        
        ansL[Level].append( root.val )
        if root.left is not None or root.right is not None:
            if len(ansL) < Level + 2:
                ansL.append([])
            self.NextLevel( root.left, Level+1, ansL )
            self.NextLevel( root.right, Level+1, ansL )
            
## Sol: BFS
## Time: O(N)
## Space: O(N)
class SolutionII:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        next_queue = []
        Level = []
        Ans = []
        queue = [root]
        
        while queue:
            
            for root in queue:
                if root is None: continue
                Level.append( root.val )
                next_queue.append( root.left )
                next_queue.append( root.right )
                
            queue = next_queue
            next_queue = []
            if not len(Level): continue
            Ans.append( Level )
            Level = []
        
        return Ans
