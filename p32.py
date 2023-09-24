# Python Program to find the sum of natural numbers using recursion

def sum_n(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    else:
        return num + sum_n(num-1)
    
num = int(input("Enter number:"))
if num<=0:
    print("Enter a positive number")
else:
    print(sum_n(num))