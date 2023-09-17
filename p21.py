# Python Program to find the sum of Natural numbers

# method - 1
num = int(input("Enter the number:"))

sum = 0
if num>0:
    for i in range(1,num+1):
        sum += i
    print(f"Sum:{sum}")
else:
    print("Number cannot be negative or zero")

# method - 2
# num = int(input("Enter the number:"))

# sum = num*(num+1)/2

# print(f"Sum:{int(sum)}")