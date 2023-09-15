# Python Program to print all prime number in an interval

start = int(input("Enter start point:"))
end = int(input("Enter end point:"))


for i in range(start,end+1):
    if i > 1:
        for j in range(2,i):
            if i%j == 0:
                break
        else:
            print(f"{i} is a prime number") 