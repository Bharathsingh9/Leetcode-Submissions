# Last updated: 7/9/2026, 9:05:29 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isBalanced(self, root: Optional[TreeNode]) -> bool:
9        balanced = [True]
10        
11        def height(root):
12            if not root:
13                return 0
14
15            left_height = height(root.left)
16            right_height = height(root.right)
17            
18            if abs(left_height - right_height) > 1:
19                balanced[0] = False
20                return 0
21
22            return 1 + max(left_height, right_height)
23
24        height(root)
25        return balanced[0]