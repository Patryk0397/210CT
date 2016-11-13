
def prime(n,counter=2):     #Counter starts at 2 because if it started at 1 all numbers would be prime
    if n == 0:              # Base Case
        return True
    elif n == 1:            #If n is 1, return True because 1 is a prime number
        return True
    elif n == counter:      #If counter gets to n number is a prime as n%n and n%1 = Prime
        return True
    elif (n%counter) == 0:  #If any counter value gets a 0 after doing modulo number is not a prime
        return False
    else:
        return prime(n,counter+1)   #Recursion - Adds to the counter each time
    
