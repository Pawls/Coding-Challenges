class Node:

    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None

class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.total_nodes = None

    def __str__(self):
        q = [self.root]

        count = 1
        while q:
            node = q.pop()
            print('Node #)
            if node.left:
                q.insert(0, node.left)
                count += 1
            if node.right:
                q.insert(0, node.right)
                count += 1

    
    def add(self, value):
        self.total_nodes += 1
        node = Node(value)
        if not self.root:
            self.root = node
        else:
            ptr = self.root
            while ptr:
                if ptr.value > value:
                    if not ptr.left:
                        ptr.left = node
                        break
                    ptr = ptr.left
                elif ptr.value < value:
                    if not ptr.right:
                        ptr.right = node
                        break
                    ptr = ptr.right

def minimal_tree(arr):
    if not arr:
        return None
    middle = len(arr) // 2
    node = Node(arr[middle])
    node.left = minimal_tree(arr[:middle])
    node.right = minimal_tree(arr[middle+1:])

    return node
