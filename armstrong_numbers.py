def is_armstrong_number(number):
    """Checks if a given number is an armstrong Number.
    
    :param number: int 
    :return: bool - Whther the number is armstrong or not."""
    return True if (sum(int(digit)**len(str(number)) for digit in str(number)) == number) else False
    
        