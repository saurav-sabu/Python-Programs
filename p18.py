# Python Program to print the fibonacci series

num = int(input("Enter the num:"))
a = 0
b = 1

if num == 1:
    print(a,end=" ")
else:
    print(a,end=" ") 
    print(b,end=" ")
    for i in range(num-2):
        c = a+b
        print(c,end=" ")
        a = b
        b = c

