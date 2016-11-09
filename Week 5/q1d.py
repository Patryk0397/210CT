def longestSequence(sequence, subList, List):

    for i in range(0, len(sequence)):
        if i == 0:
            subList.append(sequence[i])

        elif sequence[i] > sequence[i-1]:
            subList.append(sequence[i])

        else:
            List.append(subList)
            print('jshfjksdhf',List)
            subList[:] = []


    print(List)

longestSequence([1,2,3,4,2,3,1,2,3,4,5],[],[])
                
