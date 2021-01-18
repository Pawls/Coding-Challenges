from Graph import Graph

def build_order(graph):
    result = []
    hashmap = graph.adjacency.copy()
    while hashmap:
        independent = None
        for key,value in hashmap.items():
            if not value:
                hashmap.pop(key)
                independent = key
                result.append(independent)
                break
        if independent:
            for project,dependencies in hashmap.items():
                if independent in dependencies:
                    dependencies.remove(independent)
    return result
                          

graph = Graph()
graph.addVertex('a','b','c','d','e','f')
graph.addEdge('d','a')
graph.addEdge('b','f')
graph.addEdge('d','b')
graph.addEdge('a','f')
graph.addEdge('c','d')
print(graph)
print(build_order(graph))
