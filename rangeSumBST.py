# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def helper(root):
            if not root:
                return 0
            l = helper(root.left)
            r = helper(root.right)
            if root.val <= high and root.val >= low:
                return root.val + l + r
            return l + r
        return helper(root)