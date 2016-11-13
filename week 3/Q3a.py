def main():
    string = list(input("Please input a string: "))     #Gets the String from user
    counter = 0                                         #Sets the counter to 0
    print(vowelSearch(string,counter))                #Calls the removing function
    


    
def vowelSearch(string,counter):
    vowels = ['a','e','i','o','u']      #Array of vowels


    while counter < len(string):        #Base Case
        for i in vowels:                #Iterates through the vowels list
            if i in string:             #checks if currently checked vowel is in string
                string.remove(i)        #If it is , then it removes that vowel from the string
                vowelSearch(string, counter)  #RECURSION!! - checks for the same vowel again
            else:                   
                counter += 1            #If it doesnt find the vowel again, it goes to the next vowel


    #Changes the list of characters into a single string
    finalString = ""
    for i in string:
        finalString += i


        
    return finalString                    #Returns the result
    
main()
    
