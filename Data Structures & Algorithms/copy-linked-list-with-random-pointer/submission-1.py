"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #making a copy of the nodes and puting them in a hashmap
        oldToCopy = {None:None}
        cur = head
        
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur]=copy
            cur = cur.next

        #Add pointers and randoms
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        return oldToCopy[head]





        