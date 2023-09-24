# Python Program to find factorial of a number using recursion

def factorial(num):

    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num-1)
    

num = int(input("Enter a number:"))
if num<0:
    print("Enter a positive number")
else:
    print(factorial(num))