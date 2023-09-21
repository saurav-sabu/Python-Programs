# Python Program to find HCF or GCD

def HCF(x,y):

    if x>y:
        small = y
    else:
        small = x

    for i in range(1,small+1):
        if (x%i == 0) and (y%i == 0):
            hcf = i

    return hcf

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

print(f"HCF of {num1} and {num2}:",HCF(num1,num2))