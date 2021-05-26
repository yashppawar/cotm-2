import pandas as pd
import numpy as np
import random
'''
This piece of code adds some noise to the data and saves it.
'''

def are_limits_valid(*limits) -> bool:
    '''checks if the limits are valid or not'''
    for limit in limits:
        if not (limit is int or limit is float):
            return False
    return True


def validate_limits(limits:tuple) -> bool:
    '''Validates the given limits and raises errors if limits are not valid'''
    if len(limits) != 2:
        raise ValueError('The limits are not the reuired shape')
    if are_limits_valid(*limits):
        raise ValueError('Invalid limit types')


def get_unique_random_numbers(n:int, limits:tuple) -> list:
    '''Returns a set of unique random numbers'''
    numbers = set()
    validate_limits(limits)
    if limits[1] - limits[0] < n:
        raise ValueError('invalid set of limits, this will cause this function to run infinately!')

    while len(numbers) < abs(n):
        numbers.add(random.randrange(*limits))

    return list(numbers)


if __name__ == "__main__":
    data = pd.read_csv('data/Monthly_data_cmo.csv')
    no_noise_to = ['date', 'Year', 'Month']  # don't add noise to thsese columns

    for key, values in data.iteritems():
        if key in no_noise_to:
            continue  # do nothing

        indexes = get_unique_random_numbers(50, (0, len(data)))
        values[indexes] = np.nan

    data.to_csv('data/data_cmo_noisy.csv', index=False)        
