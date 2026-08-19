# Last updated: 8/19/2026, 8:59:27 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
9        res = []
10        def postorder(root):
11            if not root:
12                return 
13            postorder(root.left)
14            postorder(root.right)
15            res.append(root.val)
16        postorder(root)
17        return res