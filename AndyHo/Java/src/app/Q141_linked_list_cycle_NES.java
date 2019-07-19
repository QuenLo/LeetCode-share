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

public class Q141_linked_list_cycle_NES {
    
    class ListNode {
        int val;
        ListNode next;
        ListNode(int x) {
            val = x;
            next = null;
        }
    }
    
    public boolean hasCycle(ListNode head)
    {
        if( head == null ) return false;

        ListNode slow = head;
        ListNode fast = head.next;
        
        while( slow != fast )
        {
            // slow pointer will never catch up since no cycle
            if( fast == null || fast.next == null ) return false;
            
            slow = slow.next;
            fast = fast.next.next;
        }
        // for the case slow == fast that makes the program exit the while loop
        return true;
    }
}