

class Graph:

    def __init__(self):
        self.vertices = []
        self.edges = []


    def addEdge(self,a,b):
        edge = [a,b]
        self.edges.append(edge)

    def addVertex(self,label):
        self.vertices.append(label)

    def printGraph(self):
        for i in range (0,len(self.edges)):      
            for x in range(0,len(self.vertices)):
                print ((self.vertices[x]),":", (self.edges[i]))

if __name__ == "__main__":
    g = Graph()
    g.addVertex(7)
    g.addEdge(5,6)
    g.addVertex(6)
    g.addEdge(7,3)
    g.addVertex(5)
    g.addEdge(7,3)
    g.addVertex(3)
    g.addEdge(5,6)
    g.printGraph()
