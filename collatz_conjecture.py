def steps(number):
    """Calculates the number of steps taken in the collatz conjencture game.
    
    :param number: int 
    :retun: int - The number of steps taken.
    
    If number is even, divide number by 2 to get number / 2. 
    If number is odd, multiply number by 3 and add 1 to get 3*number + 1.
    Repeat the process until the number obtained is 1.
    """
    steps_count = 0
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    while number != 1:
        if number % 2 == 0:
            steps_count += 1
            number = number//2
        else:
            steps_count += 1
            number = 3*number + 1
    return steps_count
    
    
