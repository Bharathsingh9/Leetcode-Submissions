# Last updated: 8/20/2026, 12:16:36 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7from collections import deque
8class Solution:
9    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
10        if not root:
11            return []
12        res = []
13        queue = deque([root])
14        while queue:
15            l = []
16            size = len(queue)
17            for i in range(size):
18                n = queue.popleft()
19                l.append(n.val)
20                if n.left:
21                    queue.append(n.left)
22                if n.right:
23                    queue.append(n.right)
24            res.append(l)
25        return res
26        
27