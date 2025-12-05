import re


def validate_email(email: str) -> bool:
    pattern = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
    if re.match(pattern, email):
        return True
    else:
        return False

def validate_password_conditions(password: str) -> bool:
    """
    Validates 3 conditions:
    - Password must be +8 characters
    - Password must have at least 1 lowercase and 1 uppercase character
    - Password must have at least 1 symbol 
    """
    if not len(password) >= 8:
        return False
    
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_symbol = bool(re.search(r'[^a-zA-Z0-9]', password))

    return has_upper and has_lower and has_symbol # only return true if all are true