# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursive Approach
class Solution:
    def __init__(self):
        self.ans = None
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        pre_dict = collections.defaultdict(list)
        q_find, p_find = False, False
        
        def call_pre( node ):
            
            if not node:
                return False
            
            left = call_pre( node.left )
            right = call_pre(node.right)
            
            # node is one of q or p
            mid = node == q or node == p
            
            # from children or one child + itself
            if mid + left + right >= 2:
                self.ans = node
            
            return mid or left or right
        
        call_pre(root)
        
        return self.ans

class SolutionII:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        pre_dict = collections.defaultdict(list)
        q_find, p_find = False, False
        
        def call_pre( pre, node ):
            nonlocal q_find, p_find
            
            if not node:
                return
            
            if node.val == p.val:
                p_find = True
            elif node.val == q.val:
                q_find = True
                
            pre_dict[node.val].extend( pre + [node] )
            
            if p_find and q_find:
                return
            call_pre( pre_dict[node.val], node.left )
            call_pre( pre_dict[node.val], node.right )
            
        call_pre( [], root )
        p_pre = pre_dict[p.val]
        q_pre = pre_dict[q.val]
        
        for i in p_pre[::-1]:
            for j in q_pre[::-1]:
                if i == j:
                    return i
        
        
