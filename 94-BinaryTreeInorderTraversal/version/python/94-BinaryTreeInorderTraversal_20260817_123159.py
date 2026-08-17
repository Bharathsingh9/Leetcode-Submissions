# Last updated: 8/17/2026, 12:31:59 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
9        res = []
10        def inorder(root):
11            if not root:
12                return
13            inorder(root.left)
14            res.append(root.val)
15            inorder(root.right)
16        inorder(root)
17        return res