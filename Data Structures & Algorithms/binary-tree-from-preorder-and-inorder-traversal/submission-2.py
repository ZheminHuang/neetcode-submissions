# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder 中下一个要创建的节点
        preIdx = 0

        # inorder 中下一个尚未经过的位置
        inIdx = 0

        def dfs(stop_value):
            nonlocal preIdx, inIdx

            # 所有节点都已经创建
            if preIdx >= len(preorder):
                return None

            # 当前 inorder 已经到达这棵子树的边界
            # 边界之前没有节点，所以当前子树为空
            if inorder[inIdx] == stop_value:
                inIdx += 1
                return None

            # preorder 当前元素是当前子树的根
            root = TreeNode(preorder[preIdx])
            preIdx += 1

            # 左子树在 inorder 遇到当前根时结束
            root.left = dfs(root.val)

            # 右子树在当前整棵子树的外部边界处结束
            root.right = dfs(stop_value)

            return root

        # 整棵树没有真实的父级边界
        return dfs(float("inf"))