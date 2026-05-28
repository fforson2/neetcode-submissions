# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #perform bfs and always return the last value after each level
        queue = collections.deque()
        level, myList = [], []

        if root:
            queue.append(root)
        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()
                level.append(curr.val)

                if curr.left:
                    queue.append(curr.left)

                if curr.right:
                    queue.append(curr.right)

            if level:
                myList.append(level[-1])

        return myList
                
        