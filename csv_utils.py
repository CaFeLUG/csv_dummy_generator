"""
    Dummy csv generator
"""
import csv

from data_utils import clean_rows, get_n_random_combinations
from generators import email_generator, add_new_column


def parse_csv(filename, delimiter=',', quotechar='"', newline=''):
    """
        Paser csv file and return header and rows
    """
    body = []
    header = None
    with open(filename, newline=newline) as csvfile:
        reader = csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar)
        for row in reader:
            if not header:
                header = tuple(row)
            else:
                body.append(tuple(row))
    return header, body


def get_combinations(filename, delimiter, newline, quantity, quotechar):
    """
        Return combinations quantity for a file
    """
    _, rows = parse_csv(filename, delimiter, quotechar, newline)
    combinations = get_n_random_combinations(rows, quantity)
    combinations = clean_rows(combinations, rows)
    return len(combinations)


def generate_csv(filename, delimiter, newline, quantity, quotechar):
    """
        Return rows with dummy data generated
    """
    header, rows = parse_csv(filename, delimiter, quotechar, newline)
    combinations = get_n_random_combinations(rows, quantity)
    combinations = clean_rows(combinations, rows)
    header, rows = add_new_column(
        header, combinations, 'email', email_generator)
    return header, rows


def write_csv(outputfile, delimiter, newline, quotechar, header, rows):
    """
        Write csv rows in a file
    """
    with open(outputfile, 'w', newline=newline) as csvfile:
        writer = csv.writer(csvfile, delimiter=delimiter,
                            quotechar=quotechar, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)
        for row in rows:
            writer.writerow(row)
