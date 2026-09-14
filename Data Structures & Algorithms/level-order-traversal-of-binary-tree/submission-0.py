# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#           1
#       2          3
#   4      5   6      7
# result = [1]
# level = [2,3]
# queue = [2,3]
# values = [2,3]

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if  not root:
            return []
        result = []
        level = []
        queue = deque([root])
        while queue:
            values = []
            for root in queue:
                values.append(root.val)
                if root.left:
                    level.append(root.left)
                if root.right:
                    level.append(root.right)
            result.append(values)
            queue = level
            level = []
        return result