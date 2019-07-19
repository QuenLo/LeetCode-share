package app;

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */

public class Q142_linked_list_cycle_2
{
    class ListNode {
        int val;
        ListNode next;
        ListNode(int x) {
            val = x;
            next = null;
        }
    }

    public ListNode detectCycle(ListNode head)
    {
        ListNode tortoise = head;
        ListNode hare = head;
        
        // phase 1, check if cycle exist
        do
        {
            try
            {
                tortoise = tortoise.next;
                hare = hare.next.next;    
            } catch ( Exception e ) { return null; }
            
            // no cycle in linked list
            if( tortoise == null || hare == null ) return null;
        } while( tortoise != hare );
        
        // phase 2, find the cycle start point
        hare = head;
        while( tortoise != hare )
        {
            tortoise = tortoise.next;
            hare = hare.next;
        }
        return tortoise;
    }
}