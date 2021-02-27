class Node:
    total = 0
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        Node.total += 1
        #print('Nodes:', Node.total)

    def __del__(self):
        Node.total -= 1
        #print('Nodes:', Node.total)

class LinkedList:
    def __init__(self):
        # Define aliases
        self.addBack = self.append = self.add
        self.addHead = self.push = self.addFront

        # Member variables
        self.head = None
        self.tail = None

    def __len__(self):
        size = 0
        for _ in self:
            size += 1
        return size

    def __str__(self):
        ptr = self.head
        nodes = ''
        while ptr:
            if ptr.prev:
                nodes += ' <- '
            nodes += str(ptr.data)
            if ptr.next:
                nodes += ' -> '
            ptr = ptr.next
        return nodes

    def __iter__(self):
        ptr = self.head
        while ptr:
            yield ptr
            ptr = ptr.next

    def delete(self):
        self.head = self.tail = None
        del self

    def get(self, index):
        if index < 0 or len(self) <= index:
            raise IndexError('list index out of range')
        ptr = self.head
        for _ in range(index):
            ptr = ptr.next
        return ptr.data

    def pop(self):
        result = self.head.data
        self.head = self.head.next
        return result

    def set(self, index, data):
        if index < 0 or len(self) <= index:
            raise IndexError('list index out of range')
        ptr = self.head
        for _ in range(index):
            ptr = ptr.next
        ptr.data = data      

    def copy(self):
        new_ll = LinkedList()
        ptr = self.head
        while ptr:
            new_ll.add(ptr.data)
            ptr = ptr.next
        return new_ll       

    def insert(self, index, data):
        size = len(self)
        if index < 0 or size < index:
            raise IndexError('list index out of range')
        if index == 0: self.addFront(data)
        elif index == size: self.add(data)
        else:
            ptr = self.head
            prev = None
            for _ in range(index):
                prev = ptr
                ptr = ptr.next
            if ptr:
                new_node = Node(data)
                new_node.next = ptr
                prev.next = new_node
            return True             

    def add(self, *data):
        for ele in data:
            if not self.head:
                self.tail = self.head = Node(ele)
            else:
                new_node = Node(ele)
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node               

    def addFront(self, *data):
        for ele in data:
            if not self.head:
                self.tail = self.head = Node(ele)
            else:
                new_node = Node(ele)
                new_node.next = self.head
                self.head = new_node

    def indexOf(self, data):
        ptr = self.head
        index = 0
        while ptr:
            if ptr.data == data:
                return index
            ptr = ptr.next
            index += 1
        return -1

    def discard(self, data):
        ptr = self.head
        prev = None
        while ptr:
            if ptr.data == data:
                if not prev:
                    self.head = self.head.next
                elif not ptr.next:
                    self.tail = prev
                    self.tail.next = None
                else:
                    prev.next = ptr.next
                return True                    
            prev = ptr
            ptr = ptr.next
        return False

    def discardAll(self, data):
        ptr = self.head
        prev = None
        while ptr:
            if ptr.data == data:
                if not prev:
                    ptr = self.head = self.head.next
                elif not ptr.next:
                    self.tail = prev
                    self.tail.next = None
                    return
                else:
                    prev.next = ptr.next
                    prev = ptr
                    ptr = ptr.next
            else:
                prev = ptr
                ptr = ptr.next


    def remove(self, data):
        ptr = self.head
        prev = None
        while ptr:
            if ptr.data == data:
                if not prev:
                    self.head = self.head.next
                elif not ptr.next:
                    self.tail = prev
                    self.tail.next = None
                else:
                    prev.next = ptr.next
                return True                    
            prev = ptr
            ptr = ptr.next
        raise KeyError(data)

    def clear(self):
        self.__init__()

    def reverse(self):
        ptr = self.head
        while ptr:
            ptr.prev, ptr.next = ptr.next, ptr.prev
            ptr = ptr.prev

        self.head, self.tail = self.tail, self.head


def exercise2(dll):
    size = len(dll)

    if size < 3:
        dll.head = dll.tail = None
        return dll
    
    odd = size & 1
    
    if odd:
        mid = size // 2
    else:
        mid = size // 2 - 1

    counter = 0
    ptr = dll.head
    while ptr:
        if counter == mid - 1:
            if odd:
                ptr.next = ptr.next.next
                ptr.next.prev = ptr
            else:
                ptr.next = ptr.next.next.next
                ptr.next.prev = ptr
            break

        ptr = ptr.next
        counter += 1

    return dll        


if __name__ == '__main__':
    '''
    print('Building Linked List now...')
    dll = LinkedList()
    dll.add(1,2)
    dll.addBack(3)
    dll.add(4,5)
    dll.addFront(0)
    print('Length:', len(ll))
    print(ll)
    print()
    print('Discarding 1 now...')
    ll.discard(1)
    print('Length:', len(ll))    
    print(ll)
    print()
    print('Discarding 0 now...')
    ll.discard(0)
    print('Length:', len(ll))    
    print(ll)
    print()
    print('Discarding 5 now...')
    ll.discard(5)
    print('Length:', len(ll))    
    print(ll)
    print()
    print('Inserting 0 now...')
    ll.insert(0,0)
    print('Length:', len(ll))    
    print(ll)
    print()
    print('Inserting 1 now...')
    ll.insert(1,1)
    print('Length:', len(ll))    
    print(ll)
    print()
    print('Inserting 5 now...')
    ll.insert(5,5)
    print('Length:', len(ll))    
    print(ll)
    
    print()
    print('Inserting at negative index now...')
    ll.insert(-1,5)    
    print()
    print('Inserting out of bounds now...')
    ll.insert(7,5)
    print(ll)
    print('Length:', len(ll))
    print()
    print('Removing 12 now...')
    ll.remove(12)
    print('Length:', len(ll))    
    print(ll)
    
    print()
    print('Clearing now...')
    ll.clear()
    print('Length:', len(ll))    
    print(ll)
    print()
    print('Building again...')    
    ll.add(1)
    ll.add(2)
    ll.addBack(3)
    ll.add(4)
    ll.add(5)
    ll.addFront(0)
    print('Length:', len(ll))
    print(ll)
    print()
    print('Copying now...')
    ll2 = ll.copy()
    print('Length:', len(ll2))    
    print(ll2.head.data, ll2, ll2.tail.data)
    print('Removing ll2...')
    ll2.delete()
    print()
    print('Getting data at index 0,1,5 now...')
    print(ll.get(0),ll.get(1),ll.get(5))
    print()
    print('Setting data at 0,1,5 to a,b,c')
    ll.set(0,'a')
    ll.set(1,'b')
    ll.set(5,'c')
    print(ll)
    print()
    print('Push -1 now...')
    ll.push(-1)
    print('Length:', len(ll))
    print(ll)
    print()
    print('Pop now...')
    print(ll.pop())
    print('Length:', len(ll))
    print(ll)
    print()
    print("Index of 'c'...")
    print(ll.indexOf('c'))
    print()
    print('Pushing 9,8,9,9, then discardAll 9s')
    ll.push(9)
    ll.push(8)
    ll.push(9)
    ll.push(9)
    print(ll)
    ll.discardAll(9)
    print(ll)
    print()
    print('Adding 9,8,9,9, using single line')
    ll.add(9,8,9,9)
    print(ll)

    print()
    print('Testing Iter')
    seq = ''
    for ele in ll:
        seq += str(ele.data) + '<|>'
    print(seq)
    '''
    print('Building Linked List now...')
    dll = LinkedList()
    dll.add(1,2,3,4,5)

    while len(dll) > 0:
        print(dll)
        exercise2(dll)
        print(dll)
        print('=' * 15)
