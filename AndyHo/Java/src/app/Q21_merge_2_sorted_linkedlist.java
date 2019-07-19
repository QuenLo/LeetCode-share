package app;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */

class Q21_merge_2_sorted_linkedlist
{
    public class ListNode {
        int val;
        ListNode next;
        ListNode(int x) { val = x; }
    }

    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        // head node
        ListNode merge = new ListNode( 0 );
        // head node pointer
        ListNode head = merge;
        while( l1 != null && l2 != null )
        {
            if( l1.val < l2.val )
            {
                merge.next = new ListNode( l1.val );
                l1 = l1.next;
            }
            else
            {
                merge.next = new ListNode( l2.val );
                l2 = l2.next;
            }
            merge = merge.next;
        }
        while( l1 != null )
        {
            merge.next = l1;
            l1 = l1.next;
            merge = merge.next;
        }
        while( l2 != null )
        {
            merge.next = l2;
            l2 = l2.next;
            merge = merge.next;
        }
        
        return head.next;
    }
}