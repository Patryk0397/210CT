import math

class graph:

    def __init__(self):
        self.adjecencyList = {}    #Creates a dictionary
        

    def addVertex(self,vertex):
        if vertex not in self.adjecencyList:   #If input vertex isnt it dictionary it adds it
            self.adjecencyList[vertex] = []
        else:
            pass                            #If it is it does nothing and ignores it
        

    def addEdge(self,vertex,edge, weight):          #Adds an edge to the graph using 2 points
        self.adjecencyList[vertex].append({edge : weight})#Adds an edge to a vertex with a weight value
        self.adjecencyList[edge].append({vertex : weight})#Adds the vertex to the edge value (has to work both ways for AL)

    def printAL(self):
        for key in self.adjecencyList:         #Function just prints out the dictionary one value under another
            print(key, ':', self.adjecencyList[key])

    def dijkstra(self, start, end):

        D = {}
        P = {}


        for node in self.adjecencyList:
            D[node] = -1
            P[node] = ""
        D[start] = 0

        unvisitedNodes = self.adjecencyList
        print('hi',unvisitedNodes)

        while len(unvisitedNodes) > 0:
            shortest = None
            node = ""

            for temporaryNode in unvisitedNodes:
                if shortest == None:
                    shortest = D[temporaryNode]
                    node = temporaryNode
                elif D[temporaryNode] < shortest:
                    shortest = D[temporaryNode]
                    node = temporaryNode
            unvisitedNodes.remove(node)
            
            for childNode, childValue in self.adjecencyList[node].items():
                if D[childNode] < D[node] + childValue:
                    D[childNode] = D[node] + childValue
                    P[childNode] = node

        path = []

        node = end

        while not (node == start):
            if path.count(node) == 0:
                path.insert(0, node)
                node = P[node]
            else:
                break
        path.insert(0, start)
        return path
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
    g.addEdge(6,7,1)
    g.addEdge(6,8,2)
    g.addEdge(6,9,3)
    g.addEdge(7,9,4)
    g.addEdge(9,8,5)
    g.printAL()
    g.dijkstra(7,8)



