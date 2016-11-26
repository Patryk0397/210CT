import random

array = [1,2,3,4,5,6]

shuffled = []

indexes = []


def shuffling():
    while len(indexes) < len(array):  #O(N)      #Loops while lent of indexes is smaller than len of array
        a = random.randint(0,(len(array)-1))#creates a random integer that will be an index
        while a in indexes: #O(N*N)
            a = random.randint(0,(len(array)-1))#If that integer is already in indexes it creates a new one
        else:
            indexes.append(a)
    
    for i in indexes:
        shuffled.append(array[i])#loops for indexes and adds values to array according to the index


shuffling()

print("Shuffled List: ")
print(shuffled)

#Big O Notation = O(N*N)
