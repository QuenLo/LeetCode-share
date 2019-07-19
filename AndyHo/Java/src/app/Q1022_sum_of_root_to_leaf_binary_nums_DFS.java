// ref. https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/discuss/270025/JavaC%2B%2BPython-Recursive-Solution

package app;

class Q1022_sum_of_root_to_leaf_binary_nums_DFS
{
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }

    public int sumRootToLeaf(TreeNode root) {
        return dfs( root, 0 );
    }
    
    private int dfs( TreeNode root, int val )
    {
        if( root == null ) return 0;
        val = val * 2 + root.val;
        return root.left == root.right ? val : dfs( root.left, val ) + dfs( root.right, val );
    }
}