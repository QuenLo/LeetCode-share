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
        
        #keep counting until there's no next node
        while l1 or l2 or carry:
            
            v1 = v2 = 0
            # the end or not
            if l1 :
                v1 = l1.val
                l1 = l1.next
            if l2 :
                v2 = l2.val
                l2 = l2.next
            
            SumNum = v1 + v2 + carry
            carry, val = divmod(SumNum, 10)
            # create next node with SunNum
            Answer.next = ListNode( val )
            
            # to next node
            Answer = Answer.next
        
        #return without the first one node
        return StartAns.next
