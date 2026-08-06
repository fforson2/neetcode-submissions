# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        myList = []

        dq = deque()

        if root:
            dq.append(root)


        while len(dq) > 0:
            myList2 = []
            for i in range(len(dq)):
                curr = dq.popleft()
                myList2.append(curr.val)

                if curr.left:
                    dq.append(curr.left)

                if curr.right:
                    dq.append(curr.right)

            myList.append(myList2)

        return myList

            