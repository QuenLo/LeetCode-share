// ref. https://leetcode.com/problems/rotate-list/discuss/22715/Share-my-java-solution-with-explanation

package app;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Q61_rotate_list
{
    public class ListNode {
        int val;
        ListNode next;
        ListNode(int x) { val = x; }
    }

    public ListNode rotateRight(ListNode head, int k)
    {
        if( head == null ) return head;
        ListNode fast = head, slow = head;
        // 1. get the length
        int len = 1; // already at the head
        while( fast.next != null )
        {
            fast = fast.next;
            len++;
        }
        
        // 2. move the list after (len - k % len)th node to the front
        // find the "(len - k % len)th - 1" node
        int i = len - k % len - 1; // this is important!!
        while( i > 0 )
        {
            slow = slow.next;
            i--;
        }

        // 3. rotate
        fast.next = head;
        head = slow.next;
        slow.next = null;

        return head;
    }
}