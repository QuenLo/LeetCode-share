# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

### Output to Array ###
class Solution1:
    def middleNode(self, head: ListNode) -> ListNode:
        ll = []
        
        while( head ):
            ll.append( head )
            head = head.next
            
        return ll[ (len( ll ))//2  ]
        
        
###  Fast and Slow Pointer ###
class Solution2:
    def middleNode(self, head: ListNode) -> ListNode:
        fast = slow = head
        
        while( fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            
        return slow
