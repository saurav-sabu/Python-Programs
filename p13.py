# Python Program to find the largest among three numbers

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))

if a>b and a>c:
    print(f"{a} is largest number")
elif b>c:
    print(f"{b} is largest number")
else:
    print(f"{c} is largest number")