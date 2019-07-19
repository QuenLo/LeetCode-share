// ref. https://www.wikiwand.com/zh-hant/%E4%BA%8C%E5%85%83%E6%90%9C%E5%B0%8B%E6%A8%B9
// ref. https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/discuss/35220/My-Accepted-Java-Solution

package app;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Q108_convert_sorted_arr_to_binary_search_tree
{
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }
 
    public TreeNode sortedArrayToBST(int[] nums)
    {
        return helper( nums, 0, nums.length - 1 );
    }
    
    public TreeNode helper( int[] nums, int left, int right )
    {
        if( right < left ) return null;
        int mid = (left + right) / 2;

        TreeNode root = new TreeNode( nums[ mid ] );
        root.right = helper( nums, mid + 1, right );
        root.left = helper( nums, left, mid - 1 );
        return root;
    }
}