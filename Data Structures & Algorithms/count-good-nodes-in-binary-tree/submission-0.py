# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: Optional[TreeNode], max_so_far: int) -> int:
            if node is None:
                return 0

            # 当前节点是否是好节点
            count = 1 if node.val >= max_so_far else 0

            # 更新从根节点到当前节点的最大值
            new_max = max(max_so_far, node.val)

            # 当前节点的结果 + 左子树结果 + 右子树结果
            return (
                count
                + dfs(node.left, new_max)
                + dfs(node.right, new_max)
            )
        if root is None:
            return 0
        return dfs(root,root.val)