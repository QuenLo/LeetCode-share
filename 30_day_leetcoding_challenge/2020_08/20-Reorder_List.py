# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        if ( head == None or head.next == None or head.next.next == None ):
            return
        else:
            fast, slow = head, head
            
            # split
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            
            # rev
            Second = slow.next
            pre = None
            slow.next = None
            while Second:
                nextN = Second.next
                Second.next = pre
                pre = Second
                Second = nextN
            
            # comp
            while pre :
                nextN = pre
                pre = pre.next
                nextN.next = head.next
                head.next = nextN
                head = head.next.next
                
                
