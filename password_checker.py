import re

COMMON_PASSWORDS = {
    "password", "123456", "123456789", "qwerty", "12345", "12345678",
    "111111", "1234567", "password123", "123123", "admin", "p@ssword"
}

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) < 8:
        feedback.append("Password is too short (at least 8 characters)")
    elif len(password) >= 12:
        score += 2
    else:
        score += 1

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters (A-Z)")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters (a-z)")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add numbers (0-9)")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add special characters (!@#$)")

    if password.lower() in COMMON_PASSWORDS:
        feedback.append("This password is too common")
        score = 0

    for i in range(len(password) - 2):
        if ord(password[i]) == ord(password[i+1]) - 1 == ord(password[i+2]) - 2:
            feedback.append("Avoid sequential characters (e.g., 'abc')")
            score = max(0, score - 2)
            break
        if password[i:i+3].isdigit() and int(password[i+1]) == int(password[i]) + 1 and int(password[i+2]) == int(password[i]) + 2:
            feedback.append("Avoid sequential numbers (e.g., '123')")
            score = max(0, score - 2)
            break
            
    if re.search(r'(.)\1\1', password):
        feedback.append("Avoid repeating characters (e.g., 'aaa')")
        score = max(0, score - 2)
        
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    elif score <= 6:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return {"strength": strength, "score": score, "feedback": feedback}