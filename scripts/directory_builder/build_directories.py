#!/usr/bin/env python3

from pathlib import Path

import os.path

import string
string.ascii_lowercase

letters = list(string.ascii_lowercase)

base_dir = "/Users/alan/workshop/letters.alanwsmith.com/sites"

for letter in letters:
    output_name = f"{letter}.alanwsmith.com"
    print(output_name)
    dir_to_make = os.path.join(base_dir, output_name)
    print(dir_to_make)
    Path(dir_to_make).mkdir(exist_ok=True)

