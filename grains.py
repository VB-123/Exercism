"""Calculate the number of grains of wheat on a chessboard given that the number on each square doubles."""

FACTOR = 2
TOTAL_NO_OF_SQUARES = 64
def square(number):
    """Calculates the number of Grains in a given square.
    
    :param number: - int The position number of the square on the chess board.
    :return: - int The number of grains in the square.
    """
    if 1 <= number <= TOTAL_NO_OF_SQUARES:
        return FACTOR**(number - 1)
    else:
        raise ValueError("square must be between 1 and 64")


def total():
    """Calculates the total number of Grains.
    
    :return: - int The total number of grains on the chess board.
    """
    return (FACTOR**TOTAL_NO_OF_SQUARES - 1)
