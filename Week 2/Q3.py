matrix1 = [[0,0],
           [0,0],
           [0,0]]

matrix2 = [[0,0],
           [0,0],
           [0,0]]

Sum = [[0,0],
       [0,0],
       [0,0]]

def populate():

    print ("Populate Matrix 1")
    
    for y in range(len(matrix1)):      
        for x in range (len(matrix1[0])):   #Populates the matrix 1            
            print("Populating x:", x, " y:" , y)
            matrix1[y][x] = int(input("enter a number to populate:"))
            
    print ("Matrix 1: ",matrix1)
    
    print ("")
    
    print ("Populate Matrix 2")
    
    for y in range(len(matrix2)):      
        for x in range (len(matrix2[0])):       #Populates Matrix 2
            print("Populating x:", x, " y:" , y)
            matrix2[y][x] = int(input("enter a number to populate:"))
    print ("Matrix 2: ",matrix2)



def addition():
    
    for i in range(len(matrix1)):   #iterates over matrix 1
    #[0] used because it only needs the length of 1 row since all rows are same size
        for y in range(len(matrix2[0])):
            Sum[i][y] = matrix1[i][y]+matrix2[i][y] #adds the sum of i and y and adds to Sum

    print (Sum)

 

def subtraction():

    for i in range(len(matrix1)):
        for y in range(len(matrix2[0])):
            Sum[i][y] = matrix1[i][y] - matrix2[i][y] 
    print (Sum)

def multiplication():
    pass

def mainMenu():
    print ("What would you like to do?")
    print ("Enter 1 for addition of matrices")
    print ("Enter 2 for subtraction of matrices")
    print ("Enter 3 for multiplication of matrices")
    choice = int(input("Please enter the number for your choice: "))

    if choice == 1:
        populate()
        addition()
    elif choice == 2:
        populate()
        subtraction()
    elif choice == 3:
        pass
    else:
        mainMenu()

mainMenu()

