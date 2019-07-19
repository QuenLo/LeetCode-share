package app;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */

 // brute force
public class Q160_intersection_of_2_linked_lists_BF
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

        ListNode cur = headA;
        while( cur != null )
        {
            ListNode looker = headB;
            while( looker != null )
            {
                if( cur == looker ) return cur;
                looker = looker.next;
            }
            cur = cur.next;
        }
        return null;
    }
}