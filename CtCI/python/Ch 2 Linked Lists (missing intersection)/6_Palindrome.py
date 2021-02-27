from LinkedList import LinkedList

def palindrome(ll):
    ll_reverse = [x.data for x in ll]
    ll_reverse = ll_reverse[::-1]
    ptr = ll.head
    for i in range(len(ll_reverse)//2):
        if ptr.data != ll_reverse[i]:
            return False
        ptr = ptr.next
    return True

def palindrome2(ll):
    stack = []
    size = len(ll)
    index = 0
    for ele in ll:
        if index < (size//2):
            stack.append(ele.data)
        elif index > (size//2):
            pop = stack.pop()
            if pop != ele.data:
                return False
        elif size % 2 == 0:
            pop = stack.pop()
            if pop != ele.data:
                return False
        index += 1
    return len(stack) == 0

    
ll = LinkedList()
ll.add(1,2,3,2,1)
print(ll)
print(palindrome(ll))
ll.discard(2)
print(ll)
print(palindrome(ll))
ll = LinkedList()
ll.add(1,2,2,1)
print(ll)
print(palindrome(ll))
ll.discard(1)
print(ll)
print(palindrome(ll))
ll = LinkedList()
ll.add(1,1,2,1,1)
print(ll)
print(palindrome(ll))
ll.discard(2)
print(ll)
print(palindrome(ll))
