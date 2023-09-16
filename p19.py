# Python Program to check Armstrong Number

num = int(input("Enter the num:"))
temp = num
s = 0
d = 0

while num!=0:
    d = num%10
    s = s + pow(d,len(str(temp)))
    num = num//10

if s == temp:
    print(f"{temp} is an armstrong number")
else:
    print(f"{temp} is not an armstrong number")