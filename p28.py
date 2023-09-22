# Python Program to make a simple calculator

num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))

choice = input("""
1. Enter + for addition
2. Enter - for subtraction
3. Enter * for multiplication
4. Enter / for division
""")

if choice == "+":
    print("Add:",num1+num2)
elif choice == "-":
    print("Sub:",num1-num2)
elif choice == "*":
    print("Multiplication:",num1*num2)
elif choice == "/":
    print("Division:",num1/num2)  
else:
    print("Wrong option")