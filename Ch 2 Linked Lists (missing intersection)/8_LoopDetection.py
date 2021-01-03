from LinkedList import LinkedList

def loopDetection(ll):
    if not ll.head.next: return False
    slow_ptr = ll.head
    fast_ptr = ll.head
    
    while fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
        if slow_ptr == fast_ptr:
            slow_ptr = ll.head
            while slow_ptr != fast_ptr:
                slow_ptr = slow_ptr.next
                fast_ptr = fast_ptr.next
            return fast_ptr        
    return False

def loopDetection2(ll):
    if not ll.head.next: return False
    slow_ptr = ll.head
    fast_ptr = ll.head
    counter = 0
    while fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
        if slow_ptr == fast_ptr:
            cycle_node = ll.head
            if counter % 2 == 0:
                counter += 1
            for _ in range(counter):
                cycle_node = cycle_node.next
            return cycle_node        
        counter += 1
    return False


print('Cycle test 1')    
ll = LinkedList()
ll.add('a','b','c','b','e')

# Convert duplicate b's into a cycle
ll.head.next.next.next = ll.head.next

cycle = loopDetection(ll)
if cycle:
    print(cycle.data)
else:
    print(cycle)

print('Cycle test 2')    
ll = LinkedList()
ll.add('a','b','c','a','e')

# Convert duplicate a's into a cycle
ll.head.next.next.next = ll.head

cycle = loopDetection(ll)
if cycle:
    print(cycle.data)
else:
    print(cycle)

print('Cycle test 3')    
ll = LinkedList()
ll.add('a','b','c','d','e','a')

# Convert duplicate a's into a cycle
ll.tail.next = ll.head

cycle = loopDetection(ll)
if cycle:
    print(cycle.data)
else:
    print(cycle)

print('No cycle test')
ll = LinkedList()
ll.add('a','b','c','d','e')
cycle = loopDetection(ll)
if cycle:
    print(cycle.data)
else:
    print(cycle)
