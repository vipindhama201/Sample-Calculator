# Program make a simple calculator


# This function subtracts two numbers 
def subtract(x, y):
   return x - y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

# Take input from the user 
choice = input("Enter choice(1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))






elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))
