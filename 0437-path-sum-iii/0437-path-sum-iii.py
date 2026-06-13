# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix = {0: 1}  # base: one path with sum=0

        def dfs(node, currSum):
            if not node:
                return 0

            currSum += node.val
            count = prefix.get(currSum - targetSum, 0)

            prefix[currSum] = prefix.get(currSum, 0) + 1
            count += dfs(node.left, currSum)
            count += dfs(node.right, currSum)
            prefix[currSum] -= 1  # backtrack

            return count

        return dfs(root, 0)

        