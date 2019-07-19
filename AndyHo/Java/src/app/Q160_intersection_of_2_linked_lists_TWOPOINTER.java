// ref. https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/322873/java-solution

package app;

public class Q160_intersection_of_2_linked_lists_TWOPOINTER
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

        ListNode lookerA = headA;
        ListNode lookerB = headB;
        
        while( lookerA != lookerB )
        {
            if( lookerA == null )   lookerA = headB;
            else                    lookerA = lookerA.next;
            
            if( lookerB == null )   lookerB = headA;
            else                    lookerB = lookerB.next;
        }
        
        return lookerA;
    }
}