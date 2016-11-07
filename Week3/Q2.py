def main():
    n = int(input("Number: "))
    counter = n-1
    
    prime(n,counter)

    if prime(n,counter) == True:
        print("Prime")
    else:
        print("Not Prime")
    
def prime(n, counter):
    print(counter)
    if n == 1:
        return True

    elif n%counter == 0:
        return False

    elif n%counter != 0:
        if counter > 1:
            counter -= 1
            prime(n,counter)
        return True

import sys
sys.setrecursionlimit(200000000)

def p2(n,d=2):
    if n == 1:
        return True
    elif n == d:
        return True
    elif (n%2) == 0:
        return False
    else:
        return p2(n,d+1)

