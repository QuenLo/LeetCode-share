# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        
        if root == None: return TreeNode(val)
        elif root.val < val : root.right = self.insertIntoBST( root.right, val )
        else: root.left = self.insertIntoBST( root.left, val )
        
        return root
        

class SolutionII(object):
    def insertIntoBST(self, root, val):
        root_head = root
        root_val = TreeNode(val)
        while(True):
            if val < root.val:
                if root.left != None:
                    root = root.left
                else:
                    root.left = root_val
                    break
                    
            else:
                if root.right != None:
                    root = root.right
                else:
                    root.right = root_val
                    break
        return root_head
