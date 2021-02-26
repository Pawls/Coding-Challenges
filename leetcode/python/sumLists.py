# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def addTwoNumbers(self, ll1, ll2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res_head = None
        carry = 0
        while ll1 and ll2:
            result = ll1.val + ll2.val + carry
            carry = 0
            if result > 9:
                carry = 1
            if not res_head:
                res_head = ListNode(result % 10)
                ptr_add = res_head
            else:
                ptr_add.next = ListNode(result % 10)
                ptr_add = ptr_add.next
            ll2 = ll2.next
            ll1 = ll1.next
            
        while ll1:
            result = ll1.val+carry
            carry = 0
            ptr_add.next = ListNode(result % 10)
            if result > 9:
                carry = 1
            ptr_add = ptr_add.next
            ll1 = ll1.next
            
        while ll2:
            result = ll2.val+carry
            carry = 0
            ptr_add.next = ListNode(result % 10)
            if result > 9:
                carry = 1
            ptr_add = ptr_add.next
            ll2 = ll2.next
            
        if carry != 0:
            ptr_add.next = ListNode(carry)
        return res_head