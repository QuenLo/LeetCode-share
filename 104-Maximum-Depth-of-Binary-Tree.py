# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
 def maxDepth(self, root):     
    if not root:
     return 0

    tmpstack = [root]
    # for count depth
    num = 0

    while tmpstack:
        nextL = []
    
        while tmpstack:
            top = tmpstack.pop()
            if top.left:
                nextL.append(top.left)
            if top.right:
                nextL.append(top.right)
                
        tmpstack = nextL
        num += 1
    return num
