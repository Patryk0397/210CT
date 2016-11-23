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

    def DFS(self, start):
        
        self.visited = []
        self.currentValue = None
        self.currentNode = None

        self.startNode = start

        if self.startNode in self.dictionary and self.currentValue == None:
            print("current : ", self.startNode)
            self.currentValue = self.dictionary[self.startNode]
            self.visited.append(self.startNode)

        for i in self.currentValue:
            print("Current value =", i)
            print('d',self.currentValue)
            if i not in self.visited:
                self.currentNode = i
                self.visited.append(self.currentNode)
                print('hi',self.currentNode)
                self.currentValue = self.dictionary[self.currentNode]
                print(i)
                print('v',self.currentValue)
            elif i in self.visited:
                pass
                

        print('lol',self.visited)
        

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

        
