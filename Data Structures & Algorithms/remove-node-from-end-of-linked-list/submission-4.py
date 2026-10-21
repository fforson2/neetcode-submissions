# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        #create a dummy node
        #point the left pointer to it
        #right pointer pointing at head
        
        dummy = ListNode(0, head)
        left = dummy
        right = head

        #move right n distance away from left
        while n > 0:
            right = right.next
            n -= 1

        #move left and right 
        #one dist each time till right becomes null
        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next