# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        self.good =0

        def dfs(node: TreeNode, curMax) :

            if not(node): return 

            if (node.val>=curMax): 
                self.good += 1
                curMax = node.val

            dfs(node.left,curMax)
            dfs(node.right,curMax)

        dfs(root,-sys.maxsize-1)
        return self.good