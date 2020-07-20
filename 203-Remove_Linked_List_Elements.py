# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution1:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        while head:
            if head.val == val:
                head = head.next
            else:
                break
        
        if not head:
            return head
        
        head_node = head
        while head_node.next != None:
            if head_node.next.val == val:
                head_node.next = head_node.next.next
            else:
                head_node = head_node.next
                
        return head
        
class Solution2:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        HEAD = ListNode(0)
        HEAD.next = head
        
        pre, cur = HEAD, head
        
        while head:
            if head.val == val:
                pre.next = head.next
            else:
                pre = head
                
            head = head.next
        
        return HEAD.next
