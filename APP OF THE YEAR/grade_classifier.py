name = input("Enter student name: ")
m1 = float(input("Enter mark 1: "))
m2 = float(input("Enter mark 2: "))
m3 = float(input("Enter mark 3: "))

avg = (m1 + m2 + m3) / 3

if avg >= 80: grade = "A"
elif avg >= 70: grade = "B"
elif avg >= 60: grade = "C"
elif avg >= 50: grade = "D"
else: grade = "F"

status = "Pass" if avg >= 50 else "Fail"

print(f"\n--- Report Card for {name} ---")
print(f"Average: {avg:.2f}")
print(f"Grade: {grade}")
print(f"Status: {status}")

if m1 < 40 or m2 < 40 or m3 < 40:
    print("Flag: Needs intervention")