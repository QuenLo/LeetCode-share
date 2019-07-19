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
class Q1022_sum_of_root_to_leaf_binary_nums
{
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }

    int sum = 0;
    public int sumRootToLeaf(TreeNode root) {
        preorder( root, "" );
        return sum;
    }
    
    private void preorder( TreeNode root, String path )
    {
        if( root == null ) return;
        path += Integer.toString( root.val );

        // leaf
        if( root.left == null && root.right == null )
        {
            System.out.println( path );
            int val = 0;
            for( int i = path.length(); i >= 1; i-- )
                val = Integer.parseInt( path.substring( i-1, i ) ) * (int) Math.pow( 2, path.length() - i ) + val;
            sum += val;
            return;
        }
        else
        {
            preorder( root.left, path );
            preorder( root.right, path );
        }
    }
}