
def HPerfSquare(num1):
    if num1 >= 0:                               #Checks if number is >= 0
        PerfSquare = num1**(1/2)                #If it is per square is input square rooted
        PerfSquare = PerfSquare - (PerfSquare%1)#Gets rid of the decimal
        PerfSquare = PerfSquare ** 2            #squares the number to make the biggest perf sq

        print(PerfSquare)                       #prints it
        return PerfSquare                       #Returns it

    elif num1 < 0:                              #If number is -ve it just prints
        print ("Integer has to be positive")

HPerfSquare(50)

