"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        OrderL = []
        if root is None: return []
        
        def df( C_Node, Level ):
            
            if not C_Node: return
            
            if len(OrderL) < Level + 2:
                OrderL.append([])
                
            OrderL[Level].append( C_Node.val )
            
            for ch in C_Node.children:
                df( ch, Level+1 )
        
        df( root, 0 )
        # empty lest
        if not len(OrderL[-1]): OrderL.pop(-1)
        return OrderL
