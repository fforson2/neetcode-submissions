# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        node = head.next
        pointer = dummy
        total = 0 

        while node:
            if node.val != 0:
                total += node.val
                
            else:
                pointer.next = ListNode(total)
                pointer = pointer.next
                total = 0

            node = node.next


        return dummy.next
                
