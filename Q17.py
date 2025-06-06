email = input("Enter email: ")

if email.count("@") != 1:
    print("Invalid email")
else:
    username, domain = email.split("@")

    valid = True

    for char in username:
        if not (char.islower() or char.isdigit() or char in ['.', '_']):
            valid = False

    if '.' not in domain:
        valid = False

    for char in domain:
        if not (char.islower() or char.isdigit() or char == '.'):
            valid = False

    print("Valid email" if valid else "Invalid email")
