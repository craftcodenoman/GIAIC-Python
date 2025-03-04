#  Day 9 – Daily Python Challenge 🐍
# 🚀 Challenge: "Password Strength Checker" 🔐
# Aaj ka challenge hai ek password strength checker banana! Tumhe ek 
# Python program likhna hai jo user ke diye gaye password ki strength analyze kare aur bata sake ke password weak,
#  moderate ya strong hai! 💪🔑

# 🔥 Requirements:
# 1️⃣ User se password input lo.
# 2️⃣ Check karo ke password kitna strong hai:




import re

def check_password_strength(password):
    if len(password) < 6:
        return "Weak ❌ (Password is to short!)"
    
    # Strength conditions
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    # Checking strength levels
    if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
        return "Strong ✅ (MashaAllah! Strong password hai!)"
    elif len(password) >= 8:
        return "Moderate ⚠️ (Special characters add karain taake aur strong ho!)"
    else:
        return "Weak ❌ (Zyada strong password choose karo!)"

# User Input
password = input("Enter your password: ")
print("Password Strength:", check_password_strength(password))


