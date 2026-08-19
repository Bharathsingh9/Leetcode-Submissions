# Last updated: 8/19/2026, 8:55:31 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
9        res = []
10        def preorder(root):
11            if not root:
12                return 
13            res.append(root.val)
14            preorder(root.left)
15            preorder(root.right)
16        preorder(root)
17        return res