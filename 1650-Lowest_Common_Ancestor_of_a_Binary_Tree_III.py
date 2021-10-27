"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        
        pre_set = set()
        def call( node ):
            
            if not node or node in pre_set:
                return node
            pre_set.add(node)
            
            return call( node.parent )
        
        # build pre_set of p
        call(p)
        return call(q)
