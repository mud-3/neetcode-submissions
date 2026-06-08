# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def helper(root, level, result):
            if not root:
                return 
            
            if len(result) <= level:
                result.append([])

            result[level].append(root.val)

            helper(root.left, level + 1, result)
            helper(root.right, level + 1, result)
        
        solution = []
        helper(root, 0, solution)

        return solution