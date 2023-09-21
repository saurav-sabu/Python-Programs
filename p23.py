# Python Program to find numbers divisible by another number

# method - 1
num = int(input("Enter number:"))

for i in range(1,101):
    if i%num == 0:
        print(f"{i} is divisible by {num}")

# method - 2
# num = int(input("Enter number:"))

# lst = [x for x in range(1,101) if x%num == 0]
# print(lst)