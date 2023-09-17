# Python Program to display powers of 2 using anonymous function

num = int(input("Enter the number of terms:")) 

print(list(map(lambda x:2**x,[x for x in range(num+1)])))