def longestSequence(sequence, pointer, SequenceList,final):

    for i in range(0,len(sequence)):
        
        if i == 0:                              #always adds the first digit in the list
            pointer.append(i)
            
        elif i == (len(sequence)-1):            #stops iteration when the loop finishes the list
            pointer.append((len(sequence))-1)
            
        elif sequence[i] > sequence[i-1]:       #if the digit before previous is smaller dont append check next
            pass
        
        elif sequence[i] <= sequence[i-1]:      #if the digit is bigger before previous, append
            pointer.append(i-1)
            pointer.append(i)

            
    for x in range(0,len(pointer),2):           #Iterates through the pointer list
        
        seq = [pointer[x],pointer[x+1]]         #Puts two pointers into a seperate list to use as coordinates

        SequenceList.append(seq)

    
    for i in SequenceList:                      #Iterates through SequenceList
        
        finseq = []                             #List for each sequence
        for x in range (i[0], i[1]+1):          #Iterates through sequence list between the two indexes given in SequenceList
            finseq.append(sequence[x])          #Appends each number two the finseq value holder

        final.append(finseq)                    #Appends the final sequence to final list

    print ("Pointer :", pointer)
    print ("SequenceList:", SequenceList)
    print('Longest subsequence = ', max(final, key = len))  #Finds the longest sequence using max and key len.
            

    

longestSequence([1,2,3,3,4,5,6,7,8,2,3,2,3,4,5,6,7,8,9,10],[], [], [])
            
#sequence = List of values to check
#pointer = Start and end of each sequence
#SequenceList = Coordinate list, basically pointer list but with start and end of sequences seperated
#final = List of lists of sequences
