import re

def evaluate_password_strength(password):
    # Minimum length requirement
    if len(password) < 8:
        return "Weak: Password is too short"
    
    # Check for uppercase, lowercase, digit, and special character
    if not re.search("[A-Z]", password) or not re.search("[a-z]", password) or not re.search("[0-9]", password) or not re.search("[!@#$%^&*]", password):
        return "Weak: Password does not meet complexity requirements"
    
    return "Strong: Password meets complexity requirements"

# Test the function
password = input("Enter your password: ")
strength = evaluate_password_strength(password)
print(strength)