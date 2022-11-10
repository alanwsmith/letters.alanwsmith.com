#!/usr/bin/env python3


import string
from string import Template


sites = [f'<a href="https://{ltr}.alanwsmith.com">{ltr}</a>' for ltr in list(string.ascii_lowercase)]

with open('index.html') as _tmpl:
    skeleton = Template(_tmpl.read())
    output = skeleton.substitute(sites=", ".join(sites))
    with open('../../main/index.html', 'w') as _out:
        _out.write(output)



