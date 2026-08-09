age_int = input("Enter your age: ")
age = int(age_int)
def check_age_limit(age: int) -> bool:
    """Checks if age is above 18

    Args:
        age (int): Age of a person

    Returns:
        bool: True if age >= 18, False otherwise
    """
    print(f"check_age_limit({age})")
    age_limit = age >= 18
    print(age_limit)
    return
Aufruf = check_age_limit(age)


"""def check_age_limit(age: int) -> bool:
    ""Checks if age is above 18

    Args:
        age (int): Age of a person

    Returns:
        bool: True if age >= 18, False otherwise
    ""
    if age >= 18:
        return True
    else:
        return False"""
    
