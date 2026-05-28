# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #I will use a dummy node to handle the edge case of add to an empty ListNode.
        #I will have a variable named "node" which will loop through the entire ListNode and 
        #will be used to add elements to the node
        #I will compare list1 and list2 and I will add the one with the smaller value to the node
        #One edgecase will be when list is longer than the other.
        #if so I will just add the rest of the elements to our already built node since it is all sorted
        #Finally I will return dummy.next since it is the head of the list we have built now

        
        #creating my dummy node and node pointer
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next

            else:
                node.next = list2
                list2 = list2.next
            
            #Updating our node on every iteration
            node = node.next

        node.next = list1 or list2

        return dummy.next









