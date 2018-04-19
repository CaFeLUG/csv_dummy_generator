"""
    Dummy csv generator
"""
import itertools
import random


def get_n_random_combinations(rows, quantity=None):
    """
        Return a list with N random combinations of two list
    """
    combinations = list(itertools.product(*zip(*rows)))
    random.shuffle(combinations)
    return combinations[:int(quantity)] if quantity else combinations


def clean_rows(all_rows, original_rows):
    """
        Remove duplicated values and remove original rows
    """
    all_set = set(all_rows)
    original_set = set(original_rows)
    return all_set - original_set


def get_column(rows, column_number):
    """
        Return a list with the column value
    """
    return list(zip(*rows))[column_number]
