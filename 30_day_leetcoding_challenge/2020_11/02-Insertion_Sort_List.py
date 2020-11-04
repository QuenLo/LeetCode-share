# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        tempNode = resultNode = head
        while head:
            tempNode = head.next
            while tempNode:
                if head.val > tempNode.val:
                    head.val, tempNode.val = tempNode.val, head.val   
                tempNode = tempNode.next
            head = head.next
        return resultNode

## Output Limit Exceeded 
class SolutionII:
    def insertionSortList(self, head: ListNode) -> ListNode:
        
        HEAD = ListNode()
        curr = head
        
        while curr:
            pre_node = HEAD
            next_node = pre_node.next
            
            while next_node:
                print(curr.val)
                if curr.val < next_node.val:
                    break
                pre_node = next_node
                next_node = pre_node.next
            
            curr_next = curr.next
            pre_node.next = curr
            pre_node.next.next = next_node
            
            curr = curr_next
        
        return HEAD.next
            
