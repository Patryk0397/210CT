class AdjecencyList:
    def __init__(self):
        self.aList= [
                [[],[]],
                [[],[]],
                [[],[]],
                [[],[]],
                [[],[]],
                [[],[]],
                [[],[]],
                [[],[]],
                [[],[]],
                [[],[]]
                        ]
    def addVertex(self):
        for i in range(0,10):
            vertex = int(input("Vertex:"))

            finished = 0

            while finished == 0:
                print("add edges 1 by 1, enter 0000 to move to next vertex")
                edge = int(input("Edge:"))
                if edge == 0000:
                    finished = 1
                else:
                    self.aList[i][1].append(edge)
                    
            self.aList[i][0].append(vertex)
            
            
        for x in range (0,len(self.aList)):
            print(self.aList[x])


if __name__ == "__main__":
    a = AdjecencyList()
    a.addVertex()

 
