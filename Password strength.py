
print("Password Strength Checker")
password = input("Enter the password: ")
strength = 0
# Check length
if len(password) >= 8:
    strength += 1
else:
    print("Password is too short. Try at least 8 characters.")
# Check for uppercase letters
if any(char.isupper() for char in password):
    strength += 1
else:
    print("Add at least one uppercase letter.")
# Check for lowercase letters
if any(char.islower() for char in password):
    strength += 1
else:
    print("Add at least one lowercase letter.")
# Check for digits
if any(char.isdigit() for char in password):
    strength += 1
else:
    print("Add at least one number.")
# Check for special characters
special_chars = "!@#$%^&*()-_=+[]{};:,.<>/?"
if any(char in special_chars for char in password):
    strength += 1
else:
    print("Add at least one special character (!@#$ etc).")
# Final Strength Result
if strength <= 2:
    print("Strength: ❌ Weak")
elif strength == 3 or strength == 4:
    print("Strength: ⚠️ Medium")
else:
    print("Strength: ✅ Strong")
