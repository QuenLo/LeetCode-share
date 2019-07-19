/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Q328_odd_even_linked_list
{
    public class ListNode {
        int val;
        ListNode next;
        ListNode(int x) { val = x; }
    }

    public ListNode oddEvenList(ListNode head)
    {
        if( head == null ) return head;
        if( head.next == null ) return head;
        if( head.next.next == null ) return head;
        
        ListNode odd = head;
        ListNode even = head.next, head_even = even;
        while( even != null && even.next != null )
        {
            odd.next = even.next;
            odd = odd.next;
            even.next = odd.next;
            even = even.next;
        }

        odd.next = head_even;
        return head;
    }
}