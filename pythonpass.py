import re

def check_password_strength(password):
    strength = 0
    remarks = []

    # Criteria checks
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    # Count passed criteria
    if not length_error:
        strength += 1
    else:
        remarks.append("Password should be at least 8 characters long.")
    
    if not digit_error:
        strength += 1
    else:
        remarks.append("Add at least one digit.")
    
    if not uppercase_error:
        strength += 1
    else:
        remarks.append("Include at least one uppercase letter.")
    
    if not lowercase_error:
        strength += 1
    else:
        remarks.append("Include at least one lowercase letter.")
    
    if not symbol_error:
        strength += 1
    else:
        remarks.append("Include at least one special character (e.g., !, @, #).")

    # Strength Rating
    if strength == 5:
        verdict = "Strong"
    elif 3 <= strength < 5:
        verdict = "Moderate"
    else:
        verdict = "Weak"

    return verdict, remarks

# User input
password = input("Enter your password: ")
verdict, feedback = check_password_strength(password)

print(f"\nPassword Strength: {verdict}")
if feedback:
    print("Feedback:")
    for suggestion in feedback:
        print(f"- {suggestion}")
