def trailing():

    number = int(input("Enter a number: ")) #(1)

    trailing = 0                            #(1)

    for x in range (5,number+1):            #(N)
        
        fact = int(x)                       #(N)

        while fact:                         #(N*N)
            if fact % 5 == 0:               #(N*N)
                trailing+=1                 #(N*N)
                fact = fact / 5             #(N*N)
            else:
                break

    print ("There are ", trailing, "zeros") #(1)

trailing()
