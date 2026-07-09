# Last updated: 7/9/2026, 9:05:07 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxDepth(self, root: Optional[TreeNode]) -> int:
9        def dfs(root, depth):
10            if not root: return depth
11            return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))
12                       
13        return dfs(root, 0)