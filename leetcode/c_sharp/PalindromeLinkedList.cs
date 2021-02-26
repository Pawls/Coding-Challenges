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
    public bool IsPalindrome(ListNode head) {
        if (head == null) return true;
        if (head.next == null) return true;
        
        Stack<int> stack = new Stack<int>();
        int length = 0;
        var ptr = head;
        while (ptr != null) {
            stack.Push(ptr.val);
            length++;
            ptr = ptr.next;
        }
        
        ptr = head;
        for (int i = 0; i < length/2; i++) {
            if (ptr.val != stack.Pop()) {
                return false;
            }
            ptr = ptr.next;
        }
        return true;        
    }
}