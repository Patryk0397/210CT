def longestSequence (sequence, subsequence, countList):
    
    for i in range (0,len(sequence)):
        if i == 0:
            countList.append(sequence[i])
        else:
            if sequence[i] > sequence[i-1]:
                countList.append(sequence[i])
            else:
                 count = len(countList)

    print(countList)


    

longestSequence([1,2,3,4,3,4,5], [], [])
