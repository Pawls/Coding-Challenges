class Node:

    def __init__(self, data):
        self.data = data
        self.parent =self.left = self.right = None

    def __str__(self):
        q = [self]

        while q:
            string = ''
            node = q.pop()
            
            if node.left:
                q.insert(0, node.left)
                string += str(node.left.data) + ' <- '

            string += str(node.data)
                
            if node.right:
                q.insert(0, node.right)
                string += ' -> ' + str(node.right.data)

            if node.left or node.right:
                print(string)
        return ''
    
    def add(self, data):
        if data <= self.data:
            if not self.left:
                self.left = Node(data)
                self.left.parent = self
            else:
                self.left.add(data)
        elif data > self.data:
            if not self.right:
                self.right = Node(data)
                self.right.parent = self
            else:
                self.right.add(data)

def get_node(node, value):
    if not node:
        return
    if node.data == value:
        return node

    return get_node(node.left, value) or get_node(node.right, value)
        

def minimal_tree(arr, parent=None):
    if not arr:
        return None
    middle = len(arr) // 2
    node = Node(arr[middle])
    if parent:
        node.parent = parent
    node.left = minimal_tree(arr[:middle],node)
    node.right = minimal_tree(arr[middle+1:],node)
    return node

# First, move the deeper node ptr up until the depth
# matches the shallow node's depth.
# Then move each pointer to its parent until they point to the same node.
def fca(tree, n1, n2):
    n1 = get_node(tree, n1)
    n2 = get_node(tree, n2)

    if n1 == n2: return n1
    
    d1 = depth(n1)
    d2 = depth(n2)
    if d2 > d1:
        n1,n2,d1,d2 = n2,n1,d2,d1

    while d1 > d2:
        n1 = n1.parent
        d1 -= 1

    while n1 != n2:
        n1,n2 = n1.parent, n2.parent
    return n1
        

def depth(node):
    if not node:
        return 0
    return 1 + depth(node.parent)


tree = minimal_tree([2,3,5,6,7,9,10,13])
print(tree)
print(fca(tree, 2, 13).data) # 7
print(fca(tree, 2, 6).data) # 5
print(fca(tree, 9, 6).data) # 7
print(fca(tree, 3, 6).data) # 5
print(fca(tree, 2, 3).data) # 3
print(fca(tree, 3, 2).data) # 3
print(fca(tree, 2, 2).data) # 2
print(fca(tree, 7, 7).data) # 7
    
