# Python Program to check if a number is positive, negatve or zero 

num = int(input("Enter the number:"))

if num>0:
    print(f"{num} is a Positive number")
elif num == 0:
    print(f"{num}")
else:
    print(f"{num} is a Negative number")