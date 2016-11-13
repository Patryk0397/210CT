def prime(n):
    x = 1
    for i in range(2,n):
        if n == 1:
            return 1
        
        elif (n%i) == 0:
            x = 0
            break

        else:
            x = 1
            break

    if x == 0: print(n, " is not a prime number")

    else: print (n, " is a prime number")

prime(1)
