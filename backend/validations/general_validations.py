import re

def validate_email(email: str) -> bool:
    pattern = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
    if re.match(pattern, email):
        return True
    else:
        return False

def validate_password_conditions(password: str) -> bool:
    if not len(password) >= 8:
        return False
    
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))

    return has_upper and has_lower # only return true if both are true