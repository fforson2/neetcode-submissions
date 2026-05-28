# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        curr1 = curr2 = dummy

        while left > 1:
            curr1 = curr1.next
            left -= 1

        while right > 0:
            curr2 = curr2.next
            right -= 1

        endC = curr2.next #connect to the end
        curr2.next = None

        prev = None
        curr = tail = curr1.next #connect to the head

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        curr1.next = prev
        tail.next = endC

        return dummy.next

        






        