#!/usr/bin/env python3

"""

Dummy csv generator.

Usage:
  dummy_generator [--quantity=QUANTITY] [--delimiter=DELIMITER]
                  [--newline=NEWLINE] [--quotechar=QUOTECHAR]
                  [--encoding=ENCODING] FILE OUTPUT
  dummy_generator [options] FILE OUTPUT
  dummy_generator --combinations [--delimiter=DELIMITER]
                     [--newline=NEWLINE] [--quotechar=QUOTECHAR]
                     [--encoding=ENCODING] FILE
  dummy_generator --combinations [options] FILE
  dummy_generator (-h | --help)
  dummy_generator --version

Arguments:
  FILE      Input csv file
  OUTPUT    Output csv file

Options:
  -h --help                              Show this screen.
  --version                              Show version.
  -c --combinations                      Show combinations quantity for a file.
  -q QUANTITY --quantity=QUANTITY        Rows quantity [default: 1000000000].
  -d DELIMITER --delimiter=DELIMITER     Csv delimiter [default: ,].
  -n NEWLINE --newline=NEWLINE           Csv newline char [default: ].
  -e ENCODING --encoding=ENCODING        Csv encoding [default: utf-8].
  --quotechar=QUOTECHAR                  Csv quotechar [default: "].
"""
from docopt import docopt
from csv_utils import generate_csv, write_csv, get_combinations


if __name__ == '__main__':
    ARGUMENTS = docopt(__doc__, version='Dummy Generator 1.0')
    COMBINATIONS = ARGUMENTS['--combinations']
    DELIMITER = ARGUMENTS['--delimiter']
    NEWLINE = ARGUMENTS['--newline']
    QUANTITY = ARGUMENTS['--quantity']
    QUOTECHAR = ARGUMENTS['--quotechar']
    ENCODING = ARGUMENTS['--encoding']
    FILE = ARGUMENTS['FILE']
    OUTPUT = ARGUMENTS['OUTPUT']
    if COMBINATIONS:
        COMBINATIONS_QUANTITY = get_combinations(
            FILE, DELIMITER, NEWLINE, QUANTITY, QUOTECHAR, ENCODING)
        print(COMBINATIONS_QUANTITY)
    else:
        HEADER, CSV = generate_csv(
            FILE, DELIMITER, NEWLINE, QUANTITY, QUOTECHAR, ENCODING)
        write_csv(OUTPUT, DELIMITER, NEWLINE, QUOTECHAR, ENCODING, HEADER, CSV)
