# Last updated: 8/17/2026, 12:44:46 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
9        res = []
10        ans = []
11        def preorder(p):
12            if not p:
13                res.append(None)
14                return
15            res.append(p.val)
16            preorder(p.left)
17            preorder(p.right)
18        preorder(p)
19        def preorder1(q):
20            if not q:
21                ans.append(None)
22                return
23            ans.append(q.val)
24            preorder1(q.left)
25            preorder1(q.right)
26        preorder1(q)
27        return res == ans
28
29