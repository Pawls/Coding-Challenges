class Graph:

    def __init__(self):
        self.adjacency = {}

    def __str__(self):
        return str(self.adjacency)

    def __len__(self):
        return len(self.adjacency)

    def addVertex(self, *value):
        for vertex in value:
            if vertex in self.adjacency.keys():
                raise Exception('vertex already exists')
            self.adjacency[vertex] = []

    def removeVertex(self, value):
        if value not in self.adjacency.keys():
            raise KeyError('vertex does not exist')
        self.adjacency.pop(value)
        for vertex,edges in self.adjacency.items():
            for a in edges:
                if a == value:
                    edges.remove(a)

    def addEdge(self, v1, v2):
        if not {v1, v2} <= self.adjacency.keys():
            raise KeyError('vertex does not exist')
        self.adjacency[v1].append(v2)

    def removeEdge(self, v1, v2):
        if v1 not in self.adjacency:
            raise KeyError('vertex does not exist')
        if not v2 in self.adjacency[v1]:
            raise Exception('edge does not exist')
        self.adjacency[v1].remove(v2)

    def getAdjacent(self, v):
        return self.adjacency[v]

if __name__ == '__main__':

    mygraph = Graph()
    mygraph.addVertex('A', 'B', 'C')
    #mygraph.addVertex('B')
    #mygraph.addVertex('C')
    print(mygraph)
    mygraph.addEdge('A', 'B')
    mygraph.addEdge('A', 'C')
    mygraph.addEdge('C', 'B')
    print(mygraph)
    mygraph.removeEdge('A', 'C')
    print(mygraph)
    mygraph.removeVertex('B')
    print(mygraph)


