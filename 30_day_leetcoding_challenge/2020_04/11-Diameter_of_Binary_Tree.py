### Depth-First Search ###
class Solution1:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.Max = 0
        
        def diameter( root ):
            if not root:
                return 0
            
            leftd = diameter( root.left )
            rightd = diameter( root.right )
            self.Max = max( self.Max, leftd + rightd )
            return max( leftd, rightd ) + 1
        
        diameter( root )
        
        return self.Max
        
class Solution2:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.Max = 0
        
        def deep( root, depth ):
            if not root:
                return depth
            
            leftd = deep( root.left, depth + 1 )
            rightd = deep( root.right, depth + 1 )

            self.Max = max( self.Max, leftd + rightd - 2 - 2*depth )
            return max( leftd, rightd )
        
        deep( root, 0 )
        
        return self.Max
