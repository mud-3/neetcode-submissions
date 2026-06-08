# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, max_val):
            if not root:
                return 0

            count = 0
            if root.val >= max_val:
                max_val = root.val
                count = 1

            count += dfs(root.left, max_val)
            count += dfs(root.right, max_val)
            return count

        return dfs(root, root.val)