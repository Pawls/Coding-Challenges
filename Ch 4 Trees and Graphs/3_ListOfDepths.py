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

# This function uses BFS
# Works on non-balanced BSTs
def list_of_depths_bfs(tree):
    q = [tree]
    result = [[]]
    count = 0
    level = 0
    while q:
        node = q.pop()
        if node:
            result[level].append(node.value)
            
            if node.left:
                q.insert(0, node.left)
            else:
                q.insert(0, None)
                
            if node.right:
                q.insert(0, node.right)
            else:
                q.insert(0, None)
            
        count += 1
        if all(ele is None for ele in q): break
        if count == 2**level:
            count = 0
            result.append([])
            level += 1
                          
    return result

# Uses DFS
def list_of_depths_dfs(tree):
    return _list_of_depths_dfs(tree, [], 0)    

def _list_of_depths_dfs(node, result, depth):
    if depth > len(result)-1:
        result.append([])
    result[depth].append(node.value)
    if node.left:
        result = _list_of_depths_dfs(node.left, result, depth+1)
    if node.right:
        result = _list_of_depths_dfs(node.right, result, depth+1)
    return result    

tree = minimal_tree([1,2,3,4,5,6,7])
print('BFS:',list_of_depths_bfs(tree))
print('DFS:',list_of_depths_dfs(tree))
print()

tree = minimal_tree([2,3,5,6,7,9,10,13])
print('BFS:',list_of_depths_bfs(tree))
print('DFS:',list_of_depths_dfs(tree))
print()

tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.right.left = Node(5)
tree.right.right = Node(6)
#print(tree)
print('BFS:',list_of_depths_bfs(tree))
print('DFS:',list_of_depths_dfs(tree))

print('Large tree time test')
tree = minimal_tree([x for x in range(10000)])
t0 = time()
list_of_depths_bfs(tree)
t1 = time()
print('BFS Time:', (t1-t0))
t0 = time()
list_of_depths_dfs(tree)
t1 = time()
print('DFS Time:', (t1-t0))
