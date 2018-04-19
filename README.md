# CSV dummy generator

## Use
[![asciicast](https://asciinema.org/a/IfqOe0CRNRa5HYR2GEIHScBU4.png)](https://asciinema.org/a/IfqOe0CRNRa5HYR2GEIHScBU4)

## Description
Este generador toma un archivo csv y genera un archivo con las combinaciones posibles (evitando las combinaciones iniciales) y agregando un mail calculado a partir de distintas templates.

## Install
```bash
pip install -r requirements.txt
```

## Help
```bash
./dummy_generator.py -h
# OR
./dummy_generator.py --help
```

## Examples
```bash
# Create all dummy rows and save in file
./dummy_generator.py ./examples/nombreApellido.csv output.csv

# Create N dummy rows and save in file
./dummy_generator.py -q N ./examples/nombreApellido.csv output.csv
```
