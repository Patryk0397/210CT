def binarySearch(val1, val2, List):      #Function takes v(value) and a list to iterate
    first = 0                   #First Value
    last = len(List)-1          #Last Value
    found = False               #Found Boolean

    while first <= last and not found:  #Iterates while first value <= last value, and not found is True
        mid = int((first+last)/2)       #Finds the midpoint
        if (List[mid] <= val2) and (List[mid] >= val1) :#Checks if midvalue is a val between given range
            found = True                #Changes found to True when the value is found
        else:
            if (val1 < List[mid]):           #If value is less than midvalue it 
                last = mid-1            #Puts the last value to be the mid value (cuts list)
            else:
                first = mid+1           #Otherwise it makes the mid value the first value (cuts)

    if found == True:                   #Print statements to inform the user of the result
        print ( "A number between the range has been found")
    else:
        print ("A number between the range was not found")



binarySearch(-1,0, [1,2,3,4,5,8,59])
