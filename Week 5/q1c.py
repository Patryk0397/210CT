def longestSequence(sequence, subList):
    counter1 = 0
    counter2 = 0
    data = [0,0,0]

    for i in range(0,len(sequence)):

        if i == 0:
            subList.append(sequence[i])
            counter2 += 1
            
        else:
            if sequence[i] > sequence[i-1]:
                subList.append(sequence[i])
                counter2 += 1

                if counter2 > counter1:
                    
                    start = i - counter2
                    end = i
                    length = counter2

                    data[0] = start
                    data[1] = end
                    data[2] = length

            else:
                subList[:] = []


    for x in range(data[0],data[1]):
        print (sequence[x])

longestSequence([1,2,3,4,5,2,3,1,2,1,2,3,4,5,6], [])

