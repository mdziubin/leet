class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def leftSum(node, isLeft):
            if not node:
                return 0
            if isLeft and not node.left and not node.right:
                return node.val
            return leftSum(node.left, True) + leftSum(node.right, False)
        return leftSum(root, False)