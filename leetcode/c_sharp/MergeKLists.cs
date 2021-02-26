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
public class Solution
{
    public ListNode MergeTwoLists(ListNode l1, ListNode l2)
    {
        if (l1 == null) return l2;
        if (l2 == null) return l1;

        ListNode result_head = l1.val <= l2.val ? l1 : l2;

        ListNode prev;
        while (l1 != null && l2 != null)
        {
            if (l1.val <= l2.val)
            {
                // If the next node in the same list is also less than the other, continue
                if (l1.next != null && l1.next.val <= l2.val)
                {
                    l1 = l1.next;
                    continue;
                }
                var temp = l1.next;
                l1.next = l2;
                l1 = temp;
            }
            else
            {
                // If the next node in the same list is also less than the other, continue
                if (l2.next != null && l2.next.val < l1.val)
                {
                    l2 = l2.next;
                    continue;
                }
                var temp = l2.next;
                l2.next = l1;
                l2 = temp;
            }
        }
        return result_head;
    }

    public ListNode MergeKLists(ListNode[] lists)
    {
        if (lists.Length == 0) return null;
        if (lists.Length == 1) return lists[0];

        ListNode ptr = lists[0];
        for (int i = 1; i < lists.Length; i++)
        {
            ptr = MergeTwoLists(ptr, lists[i]);
        }
        return ptr;
    }
}