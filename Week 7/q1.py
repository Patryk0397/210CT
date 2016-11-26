class graph:

    def __init__(self):
        self.dictionary = {}    #Creates a dictionary

    def addVertex(self,vertex):
        if vertex not in self.dictionary:   #If input vertex isnt it dictionary it adds it
            self.dictionary[vertex] = []
        else:
            pass                            #If it is it does nothing and ignores it
        

    def addEdge(self,vertex,edge):          #Adds an edge to the graph using 2 points
        self.dictionary[vertex].append(edge)#Adds an edge to a vertex
        self.dictionary[edge].append(vertex)#Adds the vertex to the edge value (has to work both ways for AL)

    def printDict(self):
        for key in self.dictionary:         #Function just prints out the dictionary one value under another
            print(key, ':', self.dictionary[key])

    def DFS(self, vertex):
        
        self.visited = []                   #List storing all the values that have been visited
        self.stack= []                      #Creates a stack for backtracking and moving between nodes

        self.stack.append(vertex)           #Adds the starting vertex to the stack

        while self.stack != []:             #While the stack isnt empty...
            u = self.stack.pop()            #pops the value and puts it into value holder u
            if u not in self.visited:       #if u isnt already in the visited list...
                self.visited.append(u)      #it appends u to that list
                for edge in self.dictionary[u]:#it also loops through all of the edges of that vertex
                    self.stack.append(edge) #Pushes those edges onto the stack
        BFS_Text = open("DfsOutput.txt", "w")
        BFS_Text.write("DFS traversal: %s " % self.visited)
        BFS_Text.close()               

    def BFS(self,vertex):

        self.q = []                             #Creates a list q
        self.visited = []                       #List of already visited nodes

        self.q.insert(0, vertex)                #adds the starting point to the queue

        while self.q != []:                     #While the queue (q) isnt empty...
            u = self.q.pop()                    #it pops the value from the queue and holds it in u
            if u not in self.visited:           #if u isnt already in the visited list...
                self.visited.append(u)          #it appends u to visited
                for edge in self.dictionary[u]: #loops through the edges of vertex u
                    self.q.insert(0,edge)       #inserts them into the queue
        BFS_Text = open("BfsOutput.txt", "w")
        BFS_Text.write("BFS traversal: %s " % self.visited)
        BFS_Text.close()
       
        

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

#FOR BFS I have used a list instead of an actual queue to save the amount of code written as a list can be used
#as a queue if you insert values at index 0 and pop values from the end
#Therefore the first value is always the end of the queue and last value is the start of the queue
        
