# Python Program to convert Decimal to Binary using recursion

def DecToBin(num):

    if num > 1:
        DecToBin(num//2)
    
    print(num%2,end="")

DecToBin(32)