class Vertex:
    def __init__(self):
        self.edges = []




    
    
class Graph:
    def __init__(self):        
        self.vertices = []

    def addEdge(self,a,b):
        edge = [a,b]
        v = Vertex()
        v.edges.append(edge)
          

    def addVertex(self,n):
        self.vertices.append(n)


if __name__ == "__main__":
    g = Graph()
    v = Vertex()
    g.addVertex(7)
    g.addVertex(1)
    g.addVertex(3)
    g.addVertex(5)
    g.addVertex(9)
    g.addEdge(1,7)
    g.addEdge(3,9)
    g.addEdge(5,9)
    print(g.vertices, v.edges)
    
    
    
