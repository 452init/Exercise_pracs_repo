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
    print(EXPECTED_BAKE_TIME)
    
    remaining_time = EXPECTED_BAKE_TIME - elapsed_bake_time
    return remaining_time
print(bake_time_remaining.__doc__)


def preparation_time_in_minutes(number_of_layers):
    """Calculate preparation_time_in_minutes.

    :param number_of_layers: int - number of layers needed to prepare the lasagna.
    :return: int - the time taken to prepare the lasagna.

    Function that takes the number of layers as an arguement and returns the
    time taken to prepare the lasagna
    """
    PREPARATION_TIME = 2 
    time_taken = number_of_layers * PREPARATION_TIME
    return time_taken
print(preparation_time_in_minutes.__doc__)


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
    total_num_of_mins = preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
    return total_num_of_mins
print (elapsed_time_in_minutes.__doc__)