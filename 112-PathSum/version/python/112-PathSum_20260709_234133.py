# Last updated: 7/9/2026, 11:41:33 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
9        def dfs(node, curr_sum):
10            if not node:
11                return False
12                
13            curr_sum += node.val
14            # only need to check at the leaf node
15            if not node.left and not node.right:
16                return curr_sum == targetSum
17            return dfs(node.left, curr_sum) or dfs(node.right, curr_sum)
18            
19        return dfs(root,0)