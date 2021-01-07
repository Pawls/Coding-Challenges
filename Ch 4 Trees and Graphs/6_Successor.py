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

def successor(node):
    if node.right:
        return min_leaf(node.right)

    parent = node.parent
    while parent:
        if node == parent.left:
            return parent
        node = parent
        parent = parent.parent

    return None

def min_leaf(node):
    if not node:
        return
    if node.left:
        return min_leaf(node.left)
    return node

def inorder(node):
    if not node:
        return
    
    inorder(node.left)
    print(node.data)
    inorder(node.right)


tree = Node(7)
tree.add(5)
tree.add(10)
tree.add(3)
tree.add(6)
tree.add(9)
tree.add(13)
tree.add(2)
print(tree)
'''
print(min_leaf(tree).data)
print(min_leaf(tree.left).data)
print(min_leaf(tree.right).data)
inorder(tree)
'''
print(successor(tree.left.left.left).data) # 2 -> 3
print(successor(tree.left.left).data) # 3 -> 5
print(successor(tree.left).data) # 5 -> 6
print(successor(tree.left.right).data) # 6 -> 7
print(successor(tree).data) # 7 -> 9
print(successor(tree.right.left).data) # 9 -> 10
print(successor(tree.right).data) # 10 -> 13

