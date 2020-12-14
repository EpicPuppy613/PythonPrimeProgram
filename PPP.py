"""
PPP - Python Prime Program
"""
#Modules
from math import sqrt
import time
#Function
def TestForPrime(numtotest, debug=False, advanced=False):
    try:
        num = int(numtotest)
    except:
        raise ValueError("Invalid Number")
    try:
        bool(debug)
    except:
        raise TypeError("Invalid Debug Tag")
    prime_calc = num % 2
    progress = 3
    start = time.time()
    prime = True
    if sqrt(num) > 100:
        times = int(round(sqrt(num/20),0)-1)
    else:
        times = int(round(sqrt(num),0)-1)
    if prime_calc == 0:
        if debug != False:
            print("The number "+str(num)+" is not prime(Divisible by: 2)")
        if advanced != False:
            return(2)
        else:
            return(False)
    if sqrt(num) > 20:
        for c in range(0, 20):
            for i in range(3,times,2):
                prime_calc = num % progress
                progress += 2
                if prime_calc == 0:
                    prime = False
                    break
            if debug != False:
                bar = c
                bar = int(bar)
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nProgress: [" + "X" * (bar+1) + "-" * (19-bar) + "]")
            if prime == False:
                break
    else:
        for i in range(3,times,2):
            prime_calc = num % progress
            progress += 2
            if prime_calc == 0:
                prime = False
                break
    end = time.time()
    if debug != False:
        duration = round(end - start, 3)
        print("Finished in "+str(duration)+"s")
    if prime_calc == 0:
        if debug != False:
            print("The number "+str(num)+" is not prime(Divisible by: "+str(i)+")")
        if advanced != False:
            return(i)
        else:
            return(False)
    elif prime_calc != 0:
        if debug != False:
            print("The number "+str(num)+" is PRIME!!!")
        if advanced != False:
            return(0)
        else:
            return(True)