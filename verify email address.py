import re

email = input("Enter your email: \n").strip()
if re.search(r"^\w.+@\w+\.(\w+\.)?(com|edu|bd|uk)$", email, re.IGNORECASE):
    print("Valid Email")
else:
    print("Invalid Email")

