import re
import string

COMMON_PASSWORDS = [
    "password", "123456", "12345678", "qwerty", "abc123",
    "password1", "admin", "letmein", "welcome", "iloveyou"
]

def check_password_strength(password):
    score = 0
    feedback = []

    # check password length
    if len(password) < 8:
        feedback.append("too short (minimum 8 characters recommended)")
    else:
        score += 1

    # check for uppercase, lowercase, digits, and special characters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("add uppercase letters")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("add lowercase letters")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("add numbers")

    if re.search(rf"[{re.escape(string.punctuation)}]", password):
        score += 1
    else:
        feedback.append("add special characters (!@#$ etc.)")

    # check for common or weak passwords
    if password.lower() in COMMON_PASSWORDS:
        feedback.append("password is too common")
    else:
        score += 1

    # determine overall strength
    if score <= 2:
        strength = "Weak"
    elif score == 3 or score == 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return {"strength": strength, "score": score, "feedback": feedback}
