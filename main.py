def calculator():
	num1 = float(input("Enter first number: "))
	op = input("Enter operator (+, -, *, /): ")
	num2 = float(input("Enter second number: "))
	if op == "+":
		return num1 + num2
	elif op == "-":
		return num1 - num2
	elif op == "*":
		return num1 * num2
	elif op == "/":
		return "Error! Division by zero." if num2 == 0 else num1 / num2
	else:
		return "Invalid operator!"
#changes made in remote
print("Result:", calculator())



