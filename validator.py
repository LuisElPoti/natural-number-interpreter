def validator_phone_number(phone_number: str) -> bool:
    """
    Validates a Greek phone number based on the rules defined in the assignment. 
        1. When is 10 digits, the prefix must be 2 or 69
        2. When is 14 digits, the prefix must be 00302 or 003069
        3. When is not 10 or 14 digits, it is invalid

    Args:
        phone_number (str): The phone number to validate.

    Returns:
        bool: True if the phone number is valid, False otherwise.
    """

    # Check the length of the phone number
    if len(phone_number) == 10:
        # Check if the prefix is 2 or 69
        return phone_number.startswith(("2", "69"))
    elif len(phone_number) == 14:
        # Check if the prefix is 00302 or 003069
        return phone_number.startswith(("00302", "003069"))
    else:
        return False