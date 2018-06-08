# Problem
https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Scala - functional
```
/**
 * Definition for a binary tree node.
 * class TreeNode(var _value: Int) {
 *   var value: Int = _value
 *   var left: TreeNode = null
 *   var right: TreeNode = null
 * }
 */

object Solution {
  def maxDepth(root: TreeNode): Int = {
    if (root != null) search(root) // note that root can be null
    else 0
  }

  def search(node: TreeNode): Int = {
    if (isLeaf(node)) 1
    else if (node.left == null && node.right != null) search(node.right) + 1
    else if (node.left != null && node.right == null) search(node.left) + 1
    else Math.max(search(node.right), search(node.left)) + 1
  }

  def isLeaf(node: TreeNode): Boolean = {
    node.left == null && node.right == null
  }
}
```

