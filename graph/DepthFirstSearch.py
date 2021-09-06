class Graph():
    def __init__(self):
        self.node = {}
        
    def printGraph(self):
        for i in self.node.keys():
            print(i, '->', '\n  -> '.join([str(j) for j in self.node[i]]))
            
    def addEdge(self, fromNode, toNode):
        if fromNode in self.node.keys():
            self.node[fromNode].append(toNode)
        else:
            self.node[fromNode] = [toNode]
            
    def DFS(self):
        visited = [False for _ in range(len(self.node))]
        
        for startNode in range(len(self.node)):
            if not visited[startNode]:
                self.DFSRec(startNode, visited)
                
    def DFSRec(self, startNode, visited):
        visited[startNode] = True
        
        print(startNode, end= " -> ")
        
        for nextNode in self.node.keys():
            if not visited[nextNode]:
                self.DFSRec(nextNode, visited)
                    
if __name__ == '__main__':
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    g.printGraph()
    print('DFS:')
    g.DFS()
    
# 0 -> 1
#   -> 2
# 1 -> 2
# 2 -> 0
#   -> 3
# 3 -> 3
# DFS:
