class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev_min = None

class Stack:
    def __init__(self):
        self.top = None
        self.min = None

    def __str__(self):
        result = []
        ptr = self.top
        while ptr:
            result.append(ptr.value)
            ptr = ptr.next
        return str(result)

    def __len__(self):
        ptr = self.top
        count = 0
        for _ in self:
            count += 1
        return count

    def __iter__(self):
        ptr = self.top
        while ptr:
            yield ptr.value
            ptr = ptr.next        

    def push(self, *value):
        for ele in value:
            if not self.top:
                self.top = Node(ele)
                self.min = ele
            else:
                new_node = Node(ele)
                new_node.next = self.top
                self.top = new_node
            if ele < self.min:
                self.top.prev_min = self.min
                self.min = ele
                

    def pop(self):
        if self.top:
            if self.top.prev_min:
                self.min = self.top.prev_min
            result = self.top.value
            self.top = self.top.next
            if self.isEmpty():
                self.min = None
            return result
        raise IndexError('pop from empty stack')

    def peek(self):
        return self.top.value

    def isEmpty(self):
        return self.top == None

if __name__ == '__main__':
    mystack = Stack()
    mystack.push(0)
    mystack.push(1,2,3)
    print(mystack, 'len:', len(mystack))
    print('peek:',mystack.peek())
    print(mystack.pop())
    print(mystack)
    print(mystack.pop())
    print(mystack)
    print(mystack.pop())
    print(mystack, 'len:', len(mystack))
    print(mystack.pop())
    print(mystack, 'len:', len(mystack))

    
