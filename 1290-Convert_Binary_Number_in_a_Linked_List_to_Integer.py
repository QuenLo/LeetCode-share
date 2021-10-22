# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        def build_dec( node ):
            
            if not node:
                return ""
            
            return str(node.val) + build_dec( node.next )
        
        dec = build_dec(head)
        return int( dec, 2 )
        
        

class SolutionII:
    def getDecimalValue(self, head: ListNode) -> int:
        
        def build_dec( node, value ):
            
            if not node:
                return value
            
            return build_dec( node.next, value*2 + node.val)
        
        return build_dec(head, 0)
