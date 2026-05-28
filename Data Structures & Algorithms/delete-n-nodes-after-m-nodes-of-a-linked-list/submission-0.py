# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        left = right = dummy

        while left:
            count = 1
            while count <= m and left:
                left = left.next
                count += 1

            if not left:
                break

            right = left
            count = 0
            while count < n and right.next:
                right = right.next
                count += 1

            left.next = right.next
        return dummy.next
        