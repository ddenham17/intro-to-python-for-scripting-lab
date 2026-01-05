num_1 = int(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
num_2 = int(input("Enter the second number: "))

if operator == '+':
    result = num_1 + num_2
    print(f"Result: {num_1} + {num_2} = {result}")

elif operator == '-':
    result = num_1 - num_2
    print(f"Result: {num_1} - {num_2} = {result}")
        
elif operator == '*':
    result = num_1 * num_2
    print(f"Result: {num_1} * {num_2} = {result}")
        
elif operator == '/':
    if num_2 != 0:
        result = num_1 / num_2
        print(f"Result: {num_1} / {num_2} = {result}")
    else:
        print("Divide by zero error!")
        
else:
    print("Invalid operator error! Please use +, -, *, or /.")