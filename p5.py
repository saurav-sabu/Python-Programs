# Python Program to Solve quadratic equation

# method 1:
a = int(input("Enter the coefficient of a:"))
b = int(input("Enter the coefficient of b:"))
c = int(input("Enter the coefficient of c:"))

# ax^2 + bx + c = 0
D = b**2 - 4*a*c

if  D > 0:
    x1 =  (-b + (D**(0.5)))/(2*a)
    x2 =  (-b - (D**(0.5)))/(2*a)
    print(f"The square root are: {x1} and {x2}")
else:
    print("Solutions are not real")

# method 2:

# import cmath 

# a = int(input("Enter the coefficient of a:"))
# b = int(input("Enter the coefficient of b:"))
# c = int(input("Enter the coefficient of c:"))

# # ax^2 + bx + c = 0
# D = b**2 - 4*a*c

# x1 =  (-b + cmath.sqrt(D))/(2*a)
# x2 =  (-b - cmath.sqrt(D))/(2*a)
# print(f"The square root are: {x1} and {x2}")


