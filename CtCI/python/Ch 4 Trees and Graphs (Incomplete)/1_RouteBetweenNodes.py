from WeightedGraph import Graph

global steps

def routeBetweenNodes(graph, v1, v2):
    global steps
    steps = 0
    
    if v1 == v2:
        return []
    result = _routeBetweenNodes(graph, v1, v2, [])
    if not result:
        return False
    return result

def _routeBetweenNodes(graph, v1, v2, path):
    global steps

    if v1 in path:
        return []

    path.append(v1)
    best_path = []
    steps += 1
    print(steps, path)
    
    if path[-1] == v2:
        return []
    
    for a,b in graph.getAdjacent(v1):
        if a in path: continue
        backtrack = path.copy()
        new_path = _routeBetweenNodes(graph, a, v2, path)
        if new_path:
            path = new_path
        if v2 in path:
            if not best_path:
                best_path = path.copy()                
            elif len(best_path) > len(path):
                best_path = path.copy()            
        path = backtrack
        
    return best_path


mygraph = Graph()
mygraph.addVertex('a', 'b', 'c', 'd', 'e', 'f')
mygraph.addEdge('a','b', 1)
mygraph.addEdge('a','f', 1)
mygraph.addEdge('b','e', 1)
mygraph.addEdge('e','a', 1)
mygraph.addEdge('e','f', 1)
mygraph.addEdge('c','b', 1)
mygraph.addEdge('c','d', 1)
print(mygraph)

# Check if path from a to c
print(routeBetweenNodes(mygraph, 'a', 'c'))

# Check if path from a to e
print(routeBetweenNodes(mygraph, 'a', 'e'))

# Check if path from c to f
print(routeBetweenNodes(mygraph, 'c', 'f'))

# Check if path from c to c
print(routeBetweenNodes(mygraph, 'c', 'c'))
print(routeBetweenNodes(mygraph, 'a', 'f'))
