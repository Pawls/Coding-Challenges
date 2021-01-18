from time import time

class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.value)
    
    def __str__(self):
        q = [self]

        while q:
            string = ''
            node = q.pop()
            
            if node.left:
                q.insert(0, node.left)
                string += str(node.left.value) + ' <- '

            string += str(node.value)
                
            if node.right:
                q.insert(0, node.right)
                string += ' -> ' + str(node.right.value)

            print(string)
        return ''
    

def minimal_tree(arr):
    if not arr:
        return None
    middle = len(arr) // 2
    node = Node(arr[middle])
    node.left = minimal_tree(arr[:middle])
    node.right = minimal_tree(arr[middle+1:])
    return node 

def validate_BST(node):
    return _validate_BST(node, float('-inf'), float('inf'))

def _validate_BST(node, mini, maxi):
    if not node:
        return True

    if mini < node.value < maxi:
        return _validate_BST(node.left, mini, node.value) \
                and _validate_BST(node.right, node.value, maxi)
    return False

tree = minimal_tree([2,3,5,6,7,9,10,13])
print(validate_BST(tree))

tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.left.right = Node(5)
tree.left.left.left = Node(6)
#print(tree)
print(validate_BST(tree))

