"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root:
            return root
        
        Q = collections.deque( [root] )
        
        while Q:
            
            size = len(Q)
            
            for i in range(size):
                
                node = Q.popleft()
                
                if i < size-1:
                    node.next = Q[0]
                    
                if node.left:
                    Q.append( node.left )
                if node.right:
                    Q.append( node.right )
                    
        return root
