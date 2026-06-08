# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder_pointer, inorder_map = 0, {}

        for index, value in enumerate(inorder):
            inorder_map[value] = index
        
        def build(left, right):
            nonlocal preorder_pointer

            if left > right:
                return None

            value = preorder[preorder_pointer]
            root = TreeNode(value)
            preorder_pointer += 1
            index = inorder_map[value]

            root.left = build(left, index - 1)
            root.right = build(index + 1, right)

            return root
        
        return build(0, len(inorder) - 1)

