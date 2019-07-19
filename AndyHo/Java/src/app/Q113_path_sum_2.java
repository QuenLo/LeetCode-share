// ref. https://stackoverflow.com/questions/6536094/java-arraylist-copy

package app;

import java.util.*;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Q113_path_sum_II {

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }

    List<List<Integer>> sol = new ArrayList<List<Integer>>();
    
    public List<List<Integer>> pathSum(TreeNode root, int sum)
    {
        find( root, sum, new ArrayList<Integer>() );
        return sol;
    }
    
    public void find( TreeNode root, int sum, List<Integer> path)
    {
        // empty tree
        if( root == null ) return;
        
        path.add( root.val );

        if( root.right == null && root.left == null )
        {
            if( root.val == sum ) sol.add( path );
            return;
        }

        find( root.left, (sum - root.val), new ArrayList<Integer>( path ) );
        find( root.right, (sum - root.val), new ArrayList<Integer>( path ) );
        return;
    }
}