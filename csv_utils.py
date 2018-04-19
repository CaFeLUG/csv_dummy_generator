"""
    Dummy csv generator
"""
import csv

from data_utils import clean_rows, get_n_random_combinations
from generators import email_generator, add_new_column


def parse_csv(name, delimiter=',', qchar='"', newline='', encoding='utf-8'):
    """
        Paser csv file and return header and rows
    """
    body = []
    header = None
    with open(name, newline=newline, encoding=encoding) as csvfile:
        reader = csv.reader(csvfile, delimiter=delimiter, quotechar=qchar)
        for row in reader:
            if not header:
                header = tuple(row)
            else:
                body.append(tuple(row))
    return header, body


def get_combinations(filename, delimiter, newline, quantity, qchar, encoding):
    """
        Return combinations quantity for a file
    """
    _, rows = parse_csv(filename, delimiter, qchar, newline, encoding)
    combinations = get_n_random_combinations(rows, quantity)
    combinations = clean_rows(combinations, rows)
    return len(combinations)


def generate_csv(filename, delimiter, newline, quantity, qchar, encoding):
    """
        Return rows with dummy data generated
    """
    header, rows = parse_csv(filename, delimiter, qchar, newline, encoding)
    combinations = get_n_random_combinations(rows, quantity)
    combinations = clean_rows(combinations, rows)
    header, rows = add_new_column(
        header, combinations, 'email', email_generator)
    return header, rows


def write_csv(outputfile, delimiter, newline, qchar, encoding, header, rows):
    """
        Write csv rows in a file
    """
    with open(outputfile, 'w', newline=newline, encoding=encoding) as csvfile:
        writer = csv.writer(csvfile, delimiter=delimiter,
                            quotechar=qchar, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)
        for row in rows:
            writer.writerow(row)
