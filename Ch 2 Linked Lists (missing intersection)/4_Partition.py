from LinkedList import LinkedList

def partition(ll, val):
    ptr = ll.head
    count = 0
    size = len(ll)
    while count < size:
        if ptr.data < val:
            ll.addFront(ptr.data)
            ptr.data = ptr.next.data
            ptr.next = ptr.next.next
        elif ptr.data >= val:
            ll.addBack(ptr.data)
            ptr.data = ptr.next.data
            ptr.next = ptr.next.next
        count += 1

ll = LinkedList()
ll.add(6,7,8,9,5,1,2,3,4)
print(ll)
node = ll.head.next.next
partition(ll, 7)
print(ll)
