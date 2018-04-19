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


def generate_csv(filename, delimiter, newline, quantity, quotechar):
    """
        Return rows with dummy data generated
    """
    header, rows = parse_csv(filename, delimiter, quotechar, newline)
    all_combinations = get_n_random_combinations(rows, quantity)
    final_data = clean_rows(all_combinations, rows)
    _, new_rows = add_new_column(
        header, final_data, 'email', email_generator)
    return new_rows


def write_csv(outputfile, delimiter, newline, quotechar, rows):
    """
        Write csv rows in a file
    """
    with open(outputfile, 'w', newline=newline) as csvfile:
        writer = csv.writer(csvfile, delimiter=delimiter,
                            quotechar=quotechar, quoting=csv.QUOTE_MINIMAL)
        for row in rows:
            writer.writerow(row)
