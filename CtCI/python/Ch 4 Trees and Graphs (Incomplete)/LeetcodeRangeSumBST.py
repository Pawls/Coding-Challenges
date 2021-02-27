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

def range_sum_bst2(node, mini, maxi):
    if not node: return 0
    total = 0
    if mini <= node.data <= maxi:
        total += node.data

    total += range_sum_bst(node.left, mini, maxi)
    total += range_sum_bst(node.right, mini, maxi)

    return total

def range_sum_bst3(node, mini, maxi, total=0):
    if node:
    
        if mini <= node.data <= maxi:
            total += node.data

        if node.left:
            total += range_sum_bst(node.left, mini, maxi)

        if node.right:
            total += range_sum_bst(node.right, mini, maxi)

    return total

def range_sum_bst(node, mini, maxi):
    if not node: return 0

    if mini <= node.data <= maxi:
        return node.data + \
               range_sum_bst(node.left, mini, maxi) + \
               range_sum_bst(node.right, mini, maxi)
    
    return range_sum_bst(node.left, mini, maxi) + \
               range_sum_bst(node.right, mini, maxi)

tree = minimal_tree([2,3,5,6,7,9,10,13])
print(tree)
print(range_sum_bst(tree, 6, 9)) # 22
print(range_sum_bst(tree, 2, 5)) # 10
print(range_sum_bst(tree, 2, 13)) # 55
