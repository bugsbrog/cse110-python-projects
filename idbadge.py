print("Please enter the following information: ")
print()

first_name = input("First name: ")

# Displayed in ALL CAPS .upper()
last_name = input("Last name: ")

# All lowercase .lower()
email_address = input("Email address: ")
phone_number = input("Phone number: ")

# First letter is capitalized
job_title = input("Job title: ")
id_number = input("ID number: ")

print("\nThe ID Card is: ") # New blank line
print("----------------------------------------")
print(f"{last_name.upper()}, {first_name.capitalize()}")
print(f"{job_title.title()}")
print(f"ID: {id_number}")
print(f"\n{email_address.lower()}")
print(f"{phone_number}")
print("----------------------------------------")