passwords = input("Enter passwords (comma-separated): ").split(",")
valid = []

for pwd in passwords:
    if (6 <= len(pwd) <= 12):
        has_lower = any(c.islower() for c in pwd)
        has_upper = any(c.isupper() for c in pwd)
        has_digit = any(c.isdigit() for c in pwd)
        has_special = any(c in "$#@" for c in pwd)

        if has_lower and has_upper and has_digit and has_special:
            valid.append(pwd)

print(",".join(valid))
