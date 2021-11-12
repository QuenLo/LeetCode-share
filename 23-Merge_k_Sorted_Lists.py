# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        start = ListNode()
        temp = start
        pq = []
        
        for index, l in enumerate(lists):
            if l:
                pq.append( (l.val, index, l) )
                
        heapq.heapify(pq)
                
        while pq:
            val, i, node = pq[0]
            temp.next = ListNode(val)
            temp = temp.next
            
            if node.next == None:
                heapq.heappop(pq)
            else:
                heapq.heapreplace( pq, (node.next.val, i, node.next) )
                
        return start.next
