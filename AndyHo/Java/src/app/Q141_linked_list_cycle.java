package app;

import java.util.*;

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

public class Q141_linked_list_cycle {
    
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
        Set<ListNode> visited = new HashSet<ListNode>();
        while( head != null )
        {
            if( visited.contains( head ) ) return true;
            else
                visited.add( head );
            head = head.next;
        }
        return false;
    }
}