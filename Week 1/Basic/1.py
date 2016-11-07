import random

array = [1,2,3,4,5,6]

shuffled = []

indexes = []


def shuffling():
    while len(indexes) < len(array):
        a = random.randint(0,(len(array)-1))
        while a in indexes:
            a = random.randint(0,(len(array)-1))
        else:
            indexes.append(a)
    
    for i in indexes:
        shuffled.append(array[i])


shuffling()

print("Shuffled List: ")
print(shuffled)

