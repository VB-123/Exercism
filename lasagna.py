"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    time_remaining = EXPECTED_BAKE_TIME - elapsed_bake_time 
    return time_remaining




def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time (in minutes).

    :param number_of_layers : int - number of layers in the lasagna.
    :return: int - time elapsed (in minutes) for baking the lasagna.

    This function takes in the number of layers and calculates the 
    time that would br taken to prepare it.
    """
    time_making = 2 * number_of_layers #Time taken for baking a single layer = 2
    return time_making
  
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the time elapsed in baking(in minutes).

    :param number_of_layers : int - number of layers in the lasagna.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - time elapsed (in minutes) for baking the lasagna.

    This function takes in the above arguments and calculates the total time elapsed
    in baking the lasagna. The total time is the sum of time taken for all the layers
    to bake and the elapsed bake time.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time