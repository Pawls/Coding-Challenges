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

def check_balanced(node):
    if not node:
        return True
    
    left_length = branch_length(node.left)
    right_length = branch_length(node.right)

    if abs(left_length - right_length) <= 1:
        return check_balanced(node.left) and check_balanced(node.right)
    return False

def branch_length(node):
    if not node:
        return 0
    return max(branch_length(node.left), branch_length(node.right)) + 1


tree = minimal_tree([2,3,5,6,7,9,10,13])
print(check_balanced(tree))

tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.left.right = Node(5)
tree.left.left.left = Node(6)
#print(tree)
print(check_balanced(tree))
