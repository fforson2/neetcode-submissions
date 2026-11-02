/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode mergeNodes(ListNode head) {

        ListNode dummy = new ListNode(0, head);
        ListNode node = head.next; //looping variable
        ListNode curr = dummy; //valid tracker
        int total = 0;

        while (node != null){
            if (node.val != 0){
                total += node.val;

            } else{
                curr.next = new ListNode(total);
                curr = curr.next;
                total = 0;
            }

            node = node.next;

        }
        
        return dummy.next;
    }
}
