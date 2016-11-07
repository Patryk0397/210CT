def binarySearch(v, List):      #Function takes v(value) and a list to iterate
    first = 0                   #First Value
    last = len(List)-1          #Last Value
    found = False               #Found Boolean

    while first <= last and not found:  #Iterates while first value <= last value, and not found is True
        mid = int((first+last)/2)       #Finds the midpoint
        if List[mid] == v:              #Checks if midvalue is the value youre looking for
            found = True                #Changes found to True when the value is found
        else:
            if v < List[mid]:           #If value is less than midvalue it 
                last = mid-1            #Puts the last value to be the mid value (cuts list)
            else:
                first = mid+1           #Otherwise it makes the mid value the first value (cuts)

    if found == True:                   #Print statements to inform the user of the result
        print (v, "has been found")
    else:
        print (v, "was not found")



binarySearch('b', ['a','b','d','e','f'])
