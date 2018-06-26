# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        
        # create a Answer node and mark it's start node
        StartAns = Answer = ListNode(0)
        carry = 0
        
        # keep counting until one of nodes is end
        while l1 and l2:
            carry, sumval = divmod( l1.val+l2.val+carry, 10 )
            Answer.next = ListNode( sumval )
            
            # to next node
            l1 = l1.next
            l2 = l2.next
            Answer = Answer.next
            
        # if l1 or l2 still have next node
        tmplist = l1 or l2
        while tmplist:
            carry, sumval = divmod( tmplist.val+carry, 10 )
            Answer.next = ListNode( sumval )
            
            # to next node
            tmplist = tmplist.next
            Answer = Answer.next
            
        if carry != 0:
            Answer.next = ListNode(carry)
        
        #return without the first one node
        return StartAns.next
