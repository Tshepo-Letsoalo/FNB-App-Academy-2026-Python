num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

add = round(num1 + num2, 2)
sub = round(num1 - num2, 2)
mult = round(num1 * num2, 2)

print(f"Addition: {add}")
print(f"Subtraction: {sub}")
print(f"Multiplication: {mult}")

if num2 == 0:
    print("Division: Error - Cannot divide by zero")
    print("Floor Division: Error")
    print("Modulus: Error")
else:
    div = round(num1 / num2, 2)
    floor = round(num1 // num2, 2)
    mod = round(num1 % num2, 2)
    print(f"Division: {div}")
    print(f"Floor Division: {floor}")
    print(f"Modulus: {mod}")