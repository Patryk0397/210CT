class Graph:
    def __init__(self):        
        self.vertices = []              #initialise the class with a vertices array
        self.edges = []                 #and edges array
    def addEdge(self,a,b):
        if a and b in self.vertices:    #check if a and b are in the vertices list before adding edges
            edge = [a,b]                #if they are add the 2 nodes from the edge to a single array
            self.edges.append(edge)     #append that array to the edges array
        else:                           #if a or b are not vertices in the graph program stops and does nothing
            pass
            
            

    def addVertex(self,n):              #function adds a vertex to the vertices list
        self.vertices.append(n)


if __name__ == "__main__":
    g = Graph()
    g.addVertex(7)
    g.addVertex(1)
    g.addVertex(3)
    g.addVertex(5)
    g.addVertex(9)
    g.addEdge(1,7)
    g.addEdge(3,9)
    g.addEdge(5,9)
    print(g.vertices, g.edges)
    

    
    
    
    
