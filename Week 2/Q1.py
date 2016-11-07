
def HPerfSquare(num1):
    if num1 >= 0:
        PerfSquare = num1**(1/2)
        PerfSquare = PerfSquare - (PerfSquare%1)
        PerfSquare = PerfSquare ** 2

        print(PerfSquare)
        return PerfSquare

    elif num1 < 0:
        print ("Integer has to be positive")

HPerfSquare(50)
s
