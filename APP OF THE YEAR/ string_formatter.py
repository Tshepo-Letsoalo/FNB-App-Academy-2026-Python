fname = input("Enter first name: ")
sname = input("Enter surname: ")
bio = input("Enter your bio: ")

# Generate username: first initial + surname in lowercase
username = (fname[0] + sname).lower()

# Format name
full_name = (fname + " " + sname).title()

# Clean and update bio
clean_bio = bio.strip()
final_bio = clean_bio.replace("I am", "I'm")

# Display results
print(f"Username: {username}")
print(f"Full Name: {full_name}")
print(f"Bio Length: {len(final_bio)} characters")
print(f"Bio: {final_bio}")