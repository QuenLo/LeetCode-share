class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """ 
        n = 0 
        if root is None:
            return n
        array = [root]
        while(len(array)>0):
            n += 1
            array = [n.left for n in array if n.left is not None]+[n.right for n in array if n.right is not None]
        return n
