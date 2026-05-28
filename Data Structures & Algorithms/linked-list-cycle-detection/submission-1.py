# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #I will use a two pointer approach for this problem
        #A fast and a slow pointer
        #The fast pointer will move two times on every iteration and the slow will move once
        #The fast pointer will surely overlap the slow pointer if it is indeed a cycle
        #If so then I will return true
        #Otherwise if the fast pointer get to null it means it was not a cycle


        #intializing my fast and slow pointers
        fast, slow = head, head

        while fast and fast.next: #checking whether we have gotten to the end of a list
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False
        