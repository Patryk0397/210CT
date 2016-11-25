class graph:

    def __init__(self):
        self.dictionary = {}

    def addVertex(self,vertex):
        if vertex not in self.dictionary:
            self.dictionary[vertex] = []
        else:
            pass
        

    def addEdge(self,vertex,edge):
        self.dictionary[vertex].append(edge)
        self.dictionary[edge].append(vertex)

    def printDict(self):
        for key in self.dictionary:
            print(key, ':', self.dictionary[key])

    def DFS(self, vertex):
        
        self.visited = []
        self.stack= []

        self.stack.append(vertex)

        while self.stack != []:
            u = self.stack.pop()
            if u not in self.visited:
                self.visited.append(u)
                for edge in self.dictionary[u]:
                    self.stack.append(edge)
        print(self.visited)
        return(self.visited)

    def BFS(self,vertex):

        self.q = []
        self.visited = []

        self.q.insert(0, vertex)

        while self.q != []:
            u = self.q.pop()
            if u not in self.visited:
                self.visited.append(u)
                for edge in self.dictionary[u]:
                    self.q.insert(0,edge)
        print (self.visited)
       
        

if __name__ == '__main__':
    
    g = graph()

## 7 : 6                9
## 6 :      7    8      9  
## 8 : 6                9
## 9 : 6    7    8
    
    g.addVertex(7)
    g.addVertex(6)
    g.addVertex(8)
    g.addVertex(9)
    g.addEdge(6,7)
    g.addEdge(6,8)
    g.addEdge(6,9)
    g.addEdge(7,9)
    g.addEdge(9,8)
    g.printDict()
    g.DFS(7)
    g.BFS(7)

        
