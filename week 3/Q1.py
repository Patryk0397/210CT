def reverse():
    x = input ("Enter a sentence to reverse: ") #Gets a string to reverse                       O(1)
    strList = x.split()         #Splits the string into words into a list                       O(1)
    count = -1                  #Counter...                                                     O(1)
    revList = []                #Reversed list                                                  O(1)
    for i in strList:           #Loops through the non-reversed list                            O(N)
        revList.append(strList[count])  #Appends the words from the list (from the back)        O(N)
        count -= 1              #Decreases the count so next value from the left is checked     O(N)

    print (' '.join(revList))   #Converts the reversed list into a string and prints it         O(N)
            
reverse()

#The Big O Notation for this algorithm is O(N) due to the for loop involved.
