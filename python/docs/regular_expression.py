from os import getcwd
import os
from typing import NamedTuple
import re

class Token(NamedTuple):
    type:str
    value:str
    line:int
    column:int


def tokenize(code):
    keywords = {"IF","THEN","FOR","NEXT","GOSUB","RETURN"}
    token_spec = [
        ('NUMBER',   r'\d+(\.\d*)?'),  # Integer or decimal number
        ('ASSIGN',   r':='),           # Assignment operator
        ('END',      r';'),            # Statement terminator
        ('ID',       r'[A-Za-z0-9]+'),    # Identifiers
        ('OP',       r'[+\-\*\^/]'),      # Arithmetic operators
        ('NEWLINE',  r'\n'),           # Line endings
        ('SKIP',     r'[ \t]+'),       # Skip over spaces and tabs
        ('MISMATCH', r'.'),            # Any other character
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_spec)
    line_num = 1
    line_start = 0
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        column = mo.start() - line_start
        if kind == 'NUMBER':
            value = float(value) if '.' in value else int(value)
        elif kind == 'ID' and value in keywords:
            kind = value
        elif kind == 'NEWLINE':
            line_start = mo.end()
            line_num += 1
            continue
        elif kind == 'SKIP':
                continue
        elif kind == 'MISMATCH':
                raise RuntimeError(f'{value!r} unexpected on line {line_num}')
        yield Token(kind, value, line_num, column)


statements = '''
    IF quantity THEN
        total := total + price * quantity;
        tax := price * 0.05;
    ENDIF;'''


for token in tokenize(statements):
    print(token)


"""
tarzan_(123)  |r"\w+_\([0-9]*\)"
              |r"\w+_\(\d+\)"
              |r"\w+_\([\d+]*\)"
tarzan_(123). |r"\w+_\(\d+\)\."
tarzan_(123).mkv r"\w+_\(\d+\)\.[a-zA-z]{2,4}$"
"""


regex = re.compile(r"(?P<last>[-a-zA-Z]+), (?P<first>[-a-zA-Z]+)( (?P<middle>([-a-zA-Z]+)))?,: (?P<phone>(\d\d\d-)?\d\d\d-\d\d\d\d)")

file =  open(os.path.join(getcwd(),"./input.txt"),"r")
for line in file.readlines():
    result = regex.search(line)
    if result is None:
        print("Oops ,This is not a record")
    else:
        lastname = result.group("last")
        firstname = result.group('first')
        middlename = result.group("middle")
        if middlename == None:
            middlename = ""
        phone_number = result.group("phone")
        print({
            lastname:lastname,
            firstname:firstname,
            middlename : middlename
        })
file.close()


string =  "if the problem is textural use the the re module"
pattern = r"the the"
regex = re.compile(pattern)
text =  regex.sub("the",string)
print(text)

int_string =  "1 2 3 4 5"
def int_match_to_float(match_obj):
    return (match_obj.group('num')+".0")

pattern = r"(?P<num>[0-9]+)"
regex = re.compile(pattern)
print(regex.findall(int_string))
print(regex.sub(int_match_to_float,int_string))