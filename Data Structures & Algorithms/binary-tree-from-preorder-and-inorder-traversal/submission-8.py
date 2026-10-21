# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        #optimal solution

        inorderMap = {val:i for i, val in enumerate(inorder)}
        self.preIndex = 0

        def dfs(left, right):
            if left > right:
                return None
            
            rootVal = preorder[self.preIndex]
            self.preIndex += 1

            root = TreeNode(rootVal)
            mid = inorderMap[rootVal]


            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)

            return root

        return dfs(0, len(preorder) - 1)



