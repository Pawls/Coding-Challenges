from LinkedList import LinkedList

def sumLists_leetcode(self, ll1, ll2):
    ll_out = None
    ptr1 = ll1
    ptr2 = ll2

    carry = 0
    while ptr1 and ptr2:
        result = ptr1.val + ptr2.val + carry
        carry = 0
        if result > 9:
            carry = 1
        if not ll_out:
            ll_out = ListNode(result % 10)
            ptr_add = ll_out
        else:
            ptr_add.next = ListNode(result % 10)
            ptr_add = ptr_add.next
        ptr2 = ptr2.next
        ptr1 = ptr1.next
        
    while ptr1:
        ll_out.add(ptr1.val+carry)
        carry = 0
        ptr1 = ptr1.next
        
    while ptr2:
        ll_out.add(ptr2.val+carry)
        carry = 0
        ptr2 = ptr2.next
        
    if carry != 0:
        ptr_add.next = ListNode(carry)
    return ll_out

def sumLists(ll1, ll2):
    ll_out = LinkedList()
    if len(ll1) > len(ll2):
        ptr1 = ll1.head
        ptr2 = ll2.head
    else:
        ptr1 = ll2.head
        ptr2 = ll1.head

    carry = 0
    while ptr1:
        if ptr2:
            result = ptr1.data + ptr2.data + carry
            carry = 0
            if result > 9:
                carry = 1
            ll_out.add(result % 10)
            ptr2 = ptr2.next
        else:
            ll_out.add(ptr1.data+carry)
            carry = 0
        ptr1 = ptr1.next
    if carry != 0:
        ll_out.add(carry)
    return ll_out

def sumLists_forward(ll1, ll2):
    ll_out = LinkedList()
    if len(ll1) > len(ll2):
        for _ in range(len(ll1)-len(ll2)):
            ll2.addFront(0)
        ptr1 = ll1.head
        ptr2 = ll2.head
    else:
        for _ in range(len(ll2)-len(ll1)):
            ll1.addFront(0)
        ptr1 = ll2.head
        ptr2 = ll1.head


    while ptr1:
        result = ptr1.data + ptr2.data
        if result > 9:
            if ll_out.tail:
                ll_out.tail.data += 1
            else:
                ll_out.addFront(1)
        ll_out.add(result % 10)
        ptr2 = ptr2.next            
        ptr1 = ptr1.next
    return ll_out

def int_to_ll(num):
    ll = LinkedList()
    while num > 0:
        ll.add(num % 10)
        num //= 10
    return ll

def ll_to_int(ll):
    ptr = ll.head
    count = 1
    num = 0
    while ptr:
        num += ptr.data * count
        count *= 10
        ptr = ptr.next
    return num


while 1:
    print('Enter 2 ints, which will be stored in reverse order:')
    ll1 = int_to_ll(int(input()))
    print(ll1)
    print('+')
    ll2 = int_to_ll(int(input()))
    print(ll2)
    print('=')
    ll_sum = sumLists(ll1,ll2)
    print(ll_sum, 'or', ll_to_int(ll_sum))
    print('If added in forward order instead:')
    print(ll1)
    print('+')
    print(ll2)
    print('=')
    print(sumLists_forward(ll1,ll2))
    print()
