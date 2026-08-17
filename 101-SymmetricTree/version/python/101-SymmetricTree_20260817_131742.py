# Last updated: 8/17/2026, 1:17:42 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
9        res = []
10        ans = []
11        def preorder(root):
12            if not root:
13                res.append(None)
14                return
15            res.append(root.val)
16            preorder(root.left)
17            preorder(root.right)
18        def preorder1(root):
19            if not root:
20                ans.append(None)
21                return
22            ans.append(root.val)
23            preorder1(root.right)
24            preorder1(root.left)
25        preorder(root.left)
26        preorder1(root.right)
27        return res == ans