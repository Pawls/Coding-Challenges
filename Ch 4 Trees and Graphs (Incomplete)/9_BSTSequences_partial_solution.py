# This solution fails to consider depth-first insertions. It returns valid
# sequences if inserted breadth-first.

class Node:

    def __init__(self, data):
        self.data = data
        self.parent =self.left = self.right = None

    def __str__(self):
        q = [self]

        while q:
            string = ''
            node = q.pop()

            if not node.parent:
                print('Binary Tree')
                print('-----------')
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
        

def minimal_tree(arr, parent=None):
    """Returns a balanced binary search tree from an array"""
    if not arr:
        return None
    middle = len(arr) // 2
    node = Node(arr[middle])
    if parent:
        node.parent = parent
    node.left = minimal_tree(arr[:middle],node)
    node.right = minimal_tree(arr[middle+1:],node)
    return node

# Uses DFS
def list_of_depths_dfs(tree):
    """Groups nodes by depth and returns as 2D list"""
    return _list_of_depths_dfs(tree, [], 0)    

def _list_of_depths_dfs(node, result, depth):
    if depth > len(result)-1:
        result.append([])
    result[depth].append(node.data)
    if node.left:
        result = _list_of_depths_dfs(node.left, result, depth+1)
    if node.right:
        result = _list_of_depths_dfs(node.right, result, depth+1)
    return result   

def perm_gen(arr):
    """Generates permutations for the given array"""
    if len(arr) <= 1:
        yield arr
    else:
        # Generate recursive permutations until len(arr) <= 1
        for perm in perm_gen(arr[1:]):
            # insert the first element of arr into each index in perm
            for i in range(len(arr)):
                yield perm[:i] + [arr[0]] + perm[i:]

def perm_list(arr):
    """Takes a 2D list and returns permutations for each separate list"""
    result = []
    for index, row in enumerate(arr):
        result.append([])
        for perm in perm_gen(row):
            result[index].append(perm)
    return result

def bst_sequence(tree):
    """Returns all array sequences which may
    generate the given binary search tree
    """
    levels = list_of_depths_dfs(tree)
    perms = perm_list(levels)
    for solution in _bst_sequence(perms):
        print(solution)
        # This line flattens solution, which is a 2D list
        print([item for sublist in solution for item in sublist])

def _bst_sequence(arr):
    if len(arr) == 0:
        yield []
    else:
        for perm in _bst_sequence(arr[1:]):
            for i in arr[0]:
                yield [i] + perm

#tree = minimal_tree([2,3,5,6,7,9,10,13])
                
tree = minimal_tree([1,2,3,4,5,6])
#levels = list_of_depths_dfs(tree)
#print(levels)
#print()
#print(perm_list(levels))
print(tree)
bst_sequence(tree)

