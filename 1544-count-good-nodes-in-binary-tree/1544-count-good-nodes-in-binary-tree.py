class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = [0]
        def helper(root, maxi):
            if root:
                maxi = max(maxi, root.val)
                if maxi <= root.val:
                    res[0] += 1
                if root.left:
                    helper(root.left, maxi)
                if root.right:
                    helper(root.right, maxi)
        helper(root, -maxsize)
        return res[0]