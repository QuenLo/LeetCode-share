# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        
        if not root:
            return []
        
        result = []
        to_delete = set(to_delete)
        
        def dfs( node ):
            
            if node is None:
                return None
            
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            
            
            if node.val not in to_delete:
                return node
            else:
                if node.left:
                    result.append(node.left)
                if node.right:
                    result.append(node.right)
                return None
                
        dfs(root)
        if root.val not in to_delete:
            result.append( root )
        
        return result

class SolutionII:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        
        result = []
        to_delete = set(to_delete)
        
        def dfs( node, parent ):
            
            if node is None:
                return
            
            p = node.val not in to_delete
            dfs(node.left, p)
            dfs(node.right, p)
            
            
            if node.left and node.left.val in to_delete:
                node.left = None
            if node.right and node.right.val in to_delete:
                node.right = None
                    
            if node.val not in to_delete and not parent:
                result.append(node)
                
        dfs(root, False)
        return result
