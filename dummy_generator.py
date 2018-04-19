#!/usr/bin/env python3

"""

Dummy csv generator.

Usage:
  dummy_generator.py [--quantity=QUANTITY] [--delimiter=DELIMITER]
                     [--newline=NEWLINE] [--quotechar=QUOTECHAR] FILE OUTPUT
  dummy_generator.py [options] FILE OUTPUT
  dummy_generator (-h | --help)
  dummy_generator --version

Arguments:
  FILE      Input csv file
  OUTPUT    Output csv file

Options:
  -h --help                              Show this screen.
  --version                              Show version.
  -q QUANTITY --quantity=QUANTITY        Rows quantity [default: None]
  -d DELIMITER --delimiter=DELIMITER     Csv delimiter [default: ,]
  -n NEWLINE --newline=NEWLINE           Csv newline char [default: ]
  --quotechar=QUOTECHAR                  Csv quotechar [default: "]
"""
from docopt import docopt
from csv_utils import generate_csv, write_csv


if __name__ == '__main__':
    ARGUMENTS = docopt(__doc__, version='Dummy Generator 1.0')
    DELIMITER = ARGUMENTS['--delimiter']
    NEWLINE = ARGUMENTS['--newline']
    QUANTITY = ARGUMENTS['--quantity']
    QUOTECHAR = ARGUMENTS['--quotechar']
    FILE = ARGUMENTS['FILE']
    OUTPUT = ARGUMENTS['OUTPUT']
    CSV = generate_csv(FILE, DELIMITER, NEWLINE, QUANTITY, QUOTECHAR)
    write_csv(OUTPUT, DELIMITER, NEWLINE, QUOTECHAR, CSV)
