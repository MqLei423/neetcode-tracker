# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(node,big):
            nonlocal res
            if not node:
                return
            if node.val >= big:
                res += 1
                big = node.val
            dfs(node.left,big)
            dfs(node.right,big)
        dfs(root,-101)
        return res