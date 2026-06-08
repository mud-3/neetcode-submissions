# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Precompute inorder value -> index
        in_index = {val: i for i, val in enumerate(inorder)}

        pre_ptr = 0  # pointer into preorder

        def helper(left, right):
            nonlocal pre_ptr

            # no elements to construct
            if left > right:
                return None

            # root is always next preorder element
            root_val = preorder[pre_ptr]
            pre_ptr += 1
            root = TreeNode(root_val)

            # split inorder
            idx = in_index[root_val]

            # build left and right subtrees
            root.left = helper(left, idx - 1)
            root.right = helper(idx + 1, right)

            return root

        return helper(0, len(inorder) - 1)