"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        
        
        def finder(node):
            nonlocal last, first
        
            if node:
                #left
                finder(node.left)
                if last:
                    # connect last <=> itself
                    last.right = node
                    node.left = last
                else:
                    # keep the smallest node
                    first = node
                # set itself as last for next node
                last = node
                
                #right
                finder(node.right)
        
        if not root:
            return None
        
        first, last = None, None
        finder(root)
        last.right = first
        first.left = last
        
        return first
