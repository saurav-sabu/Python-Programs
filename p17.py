# Python Program to display the multiplication table

# method - 1
num = int(input("Enter the number:"))

for i in range(1,11):
    print(f"{num} X {i} = {num*i}")

# method - 2
# num = int(input("Enter the number:"))
# i = 1

# while i<11:
#     print(f"{num} X {i} = {num*i}")
#     i+=1