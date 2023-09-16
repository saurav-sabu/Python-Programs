# Python Program to find factorial of a number 

# method-1
num = int(input("Enter the number:"))
fact = 1

if num>=0:
    for i in range(1,num+1):
        fact = fact * i
    print(f"Factorial of {num} is {fact}")
else:
    print("For negative number factorial does not exist")    

# method-2
# num = int(input("Enter the number:"))

# def factorial(num):
#     if num==0:
#         return 1
#     else:
#         return num * factorial(num-1)

# print(factorial(num))
