/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode ReverseBetween(ListNode head, int left, int right) {
        if (head == null || head.next == null || left == right) return head;
        
        ListNode prev = null;
        ListNode ptr = head;
        ListNode left_bound = head;
        for (int i = 1; i <= right; i++) {
            if (i+1 == left) {
                left_bound = ptr;
            }
                        
            // Start reversing the linked list if left is reached
            if (i >= left) {
                var temp = ptr.next;
                ptr.next = prev;
                prev = ptr;
                ptr = temp;  
            } else {
                prev = ptr;
                ptr = ptr.next;
            }
        }        
        
        // Select the new head node if necessary and update "next" pointers
        if (left == 1) {
            head.next = ptr;
            head = prev;
        } else {
            left_bound.next.next = ptr;
            left_bound.next = prev;
        }
        return head;
    }
}