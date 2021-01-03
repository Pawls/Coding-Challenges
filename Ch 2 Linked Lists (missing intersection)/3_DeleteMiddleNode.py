from LinkedList import LinkedList

def deleteMiddleNode(ll, node):
    node.data = node.next.data
    node.next = node.next.next

ll = LinkedList()
ll.add(9,3,2,4,3,7,5,8,6)
print(ll)
node = ll.head.next.next
print('Deleting: ',node.data)
deleteMiddleNode(ll, node)
print(ll)
