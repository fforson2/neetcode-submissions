# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def minNodeVal(root):
            curr = root
            while curr.left:
                curr = curr.left
            return curr

        if not root:
            return root

        #Find the node
        if key > root.val:
            root.right = self.deleteNode(root.right, key)

        elif key < root.val:
            root.left = self.deleteNode(root.left, key)

        else:
            #node has been found
            #One or no child
            if not root.left:
                return root.right

            elif not root.right:
                return root.left

            else:
                #2 children
                minVal = minNodeVal(root.right)
                root.val = minVal.val
                root.right = self.deleteNode(root.right, minVal.val)

        return root









        