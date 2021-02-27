class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
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

tree = minimal_tree([1,2,3,4,5,6,7])
print(tree)

tree = minimal_tree([2,3,5,6,7,9,10,13])
print(tree)

