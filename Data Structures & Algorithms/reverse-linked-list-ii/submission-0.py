# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        curr1 = dummy
        curr2 = dummy

        #curr1 starts at a node before the left position
        while left > 1:
           curr1 = curr1.next
           left -= 1

        #curr2 starts at the right place(the right indicated)
        while right > 0:
            curr2 = curr2.next
            right -= 1

        nextPointer = curr2.next #save the next pointer before breaking
        curr2.next = None

        curr = curr1.next
        tail = curr #at the end of reversal this becomes the tail 
        prev = None

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        #linking pointers
        curr1.next = prev #the node right before our left is connect to the head of our reversed linked list
        tail.next = nextPointer #the tail is then reconnected at the end

        return dummy.next

            