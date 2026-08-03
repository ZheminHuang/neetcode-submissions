# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node:TreeNode,max_so_far: int)-> int :
            if node is None:
                return 0
            count = 1 if node.val>=max_so_far else 0

            max_new = max(max_so_far,node.val)

            return (count + dfs(node.right,max_new)+dfs(node.left,max_new))
        
        if root is None:
            return 0
        return dfs(root, root.val)