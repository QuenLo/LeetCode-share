package app;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Q109_convert_sorted_list_to_binary_search_tree
{
    public class ListNode {
        int val;
        ListNode next;
        ListNode(int x) { val = x; }
    }

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }

    public TreeNode sortedListToBST(ListNode head)
    {
        if( head == null ) return null;
        ListNode mid = findMid( head );
        TreeNode root = new TreeNode( mid.val );
        // only one element in list
        if( head == mid ) return root;

        root.left = sortedListToBST( head );
        root.right = sortedListToBST( mid.next );
        return root;
    }
    
    public ListNode findMid( ListNode head )
    {
        // The pointer used to disconnect the left half from the mid node.
        ListNode prev = null;
        ListNode slow = head;
        ListNode fast = head;
        
        while( fast != null && fast.next != null )
        {
            prev = slow;
            slow = slow.next;
            fast = fast.next.next;
        }
        
        // disconnect left portion of the list
        if( prev != null ) prev.next = null;
        
        return slow;
    }
}