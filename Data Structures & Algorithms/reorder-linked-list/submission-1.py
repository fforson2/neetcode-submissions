# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #I will solve this problem in three steps
        #First I will find the middle of my linked list
        #Second I will reverse the second half my linked list
        #Third I will merge the two list and return the head


        #Finding the middle
        #I will go with the fast and slow pointer approach

        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break #We have found the middle

        second = slow.next #This is where our second linked list starts
        #We then break the connection between the two halfs
        slow.next = None

        #reversing the second half of the linked list
        #We will initialize a previous pointer to false
        prev = None
        while second:
            nextnode = second.next #We store this so we don't loose access after reversing the linked list
            second.next = prev
            prev = second
            second = nextnode

            #prev becomes the head of my second linked list

        first , second = head, prev

        while second: #Because first will in somecase be longer than the second because of how we found the middle
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1 , tmp2










        