#!/usr/bin/env python3

# This is the one that makes the basic
# vanilla stub HTML pages for all the
# letters. Those will be replaced as
# individual letters get used for
# different frameworks. 

import string
from os.path import join

letters = list(string.ascii_lowercase)
base_dir = "/Users/alan/workshop/letters.alanwsmith.com/sites"

with open('template.html') as _tmpl:
    structure = string.Template(_tmpl.read())


letter_string = [f'<a href="https://{ltr}.alanwsmith.com/">{ltr}</a>' for ltr in letters]

for letter in letters:
    output_file = join(base_dir, f"{letter}.alanwsmith.com", "index.html")
    with open(output_file, "w") as _out:
        _out.write(
            structure.substitute(
                letter=letter,
                letter_string=" ".join(letter_string)
            )
        )


