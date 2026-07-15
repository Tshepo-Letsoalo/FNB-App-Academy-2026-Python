fname = input("Enter first name: ")
sname = input("Enter surname: ")
age = int(input("Enter age: "))
fav_num = float(input("Enter favourite number: "))

full_name = fname + " " + sname
print(f"Welcome, {full_name}!")

print(fname.upper() + " " + sname.upper())
print(fname.title() + " " + sname.title())

print(age * 12)
print(round(fav_num, 2))

print(type(fname))
print(type(sname))
print(type(age))
print(type(fav_num))