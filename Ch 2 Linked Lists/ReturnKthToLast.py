from LinkedList import LinkedList

def returnKthToLast(ll, k):
    if k > len(ll)-1 or k < 0:
        raise IndexError('invalid index')
    for a,b in enumerate(ll):
        if a == len(ll)-1-k:
            return b.data

# This function assumes that we don't know the size of ll
# and the tail node is unknown
def returnKthToLast2(ll, k):
    result_ptr = None
    ptr = ll.head
    counter = 0
    while ptr:
        if counter == k:
            result_ptr = ll.head
        elif counter > k:
            result_ptr = result_ptr.next
        ptr = ptr.next
        counter += 1
    if result_ptr:
        return result_ptr.data
    raise IndexError('invalid index')

ll = LinkedList()
ll.add(9,3,2,4,3,7,5,8,6)
print(ll)
while 1:
    print(returnKthToLast2(ll, int(input())))
