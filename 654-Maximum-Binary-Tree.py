# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        stack = []
        for num in nums:
            node = TreeNode(num)
            while stack and stack[-1].val < num:
                node.left = stack.pop()
            if stack:
                stack[-1].right = node
            stack.append(node)
        return stack[0]
        
# SolutionII-recursive
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class SolutionII(object):
    def constructMaximumBinaryTree(self, nums):
        if not nums: return None
        l, r = 0, len(nums) - 1
        root = nums.index( max(nums) )
        node = TreeNode( nums[root] )
        node.left = self.constructMaximumBinaryTree( nums[:root] )
        node.right = self.constructMaximumBinaryTree( nums[root+1:] )

        return node
