# Python Program to find Armstrong number in an interval

start = int(input("Enter starting point:"))
end = int(input("Enter ending point:"))

for i in range(start, end + 1):
    s = 0
    d = 0
    temp = i

    while i!= 0:
        d = i%10
        s = s + pow(d,len(str(temp)))
        i = i//10

    if temp == s:
        print(f"{temp} is an armstrong number")
