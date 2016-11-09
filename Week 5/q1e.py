def longestSequence(sequence, subList, List):

    pointer = 0
    
    for i in range(0,len(sequence)):

        print(i)

        if i == 0:
            subList.append(sequence[0])

        elif sequence[i] > sequence[i-1]:
            subList.append(sequence[i])
        
        else:
            sequence[i] <= (sequence[i-1])
            List.insert(pointer, subList)
            pointer += 1

            subList[:] = []

    print(List)



longestSequence([1,2,3,4,2,3,1,2,3,4,5],[],[])
            
