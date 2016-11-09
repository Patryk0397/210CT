def longestSequence(sequence, subList, List):

    for i in range(0,len(sequence)):

        if i == 0:
            subList.append(sequence[i])

        elif sequence[i] > sequence[i-1]:
            subList.append(sequence[i])

        elif sequence[i] <= sequence[i-1]:
            List.append(subList)
            subList[:] = []

    print(List)

longestSequence([2,3,4,5],[],[])
