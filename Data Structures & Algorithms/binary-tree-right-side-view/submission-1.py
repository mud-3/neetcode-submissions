# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_side_view = []
        current_level = 0

        def bfs(head, level, view):
            if head is None:
                return

            if len(view) <= level:
                view.append(head.val)
            else:
                view[level] = head.val

            bfs(head.left, level + 1, view)
            bfs(head.right, level + 1, view)

        bfs(root, current_level, right_side_view)

        return right_side_view