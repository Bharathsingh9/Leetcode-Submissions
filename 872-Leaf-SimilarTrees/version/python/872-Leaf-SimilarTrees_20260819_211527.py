# Last updated: 8/19/2026, 9:15:27 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
9        def get_leaves(root):
10            leaves = []
11            def dfs(node):
12                if not node:
13                    return
14                if not node.left and not node.right:
15                    leaves.append(node.val)
16                    return
17                dfs(node.left)
18                dfs(node.right)
19            dfs(root)
20            return leaves
21        return get_leaves(root1) == get_leaves(root2)
22        
23