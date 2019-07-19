package app;

import java.util.*;

public class Q160_intersection_of_2_linked_lists_SET
{

    class ListNode {
        int val;
        ListNode next;
        ListNode(int x) {
            val = x;
            next = null;
        }
    }

    public ListNode getIntersectionNode(ListNode headA, ListNode headB)
    {
        if( headA == null || headB == null ) return null;

        Set<ListNode> record = new HashSet<ListNode>();
        
        while( headA != null )
        {
            record.add( headA );
            headA = headA.next;
        }
        // find the start point of the intersection
        while( headB != null )
        {
            if( record.contains( headB ) ) return headB;
            headB = headB.next;
        }
        
        return null;
    }
}