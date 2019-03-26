#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

"""Valid Number

Validate if a given string can be interpreted as a decimal number.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

Note: It is intended for the problem statement to be ambiguous. 
You should gather all requirements up front before implementing one. 
However, here is a list of characters that can be in a valid decimal number:

Numbers 0-9
Exponent - "e"
Positive/negative sign - "+"/"-"
Decimal point - "."
Of course, the context of these characters also matters in the input.
"""

import re

numbers = [
    {'str': "0",        'res': True},
    {'str': " 0.1 ",    'res': True},
    {'str': "1 a",      'res': False},
    {'str': "abc",      'res': False},
    {'str': "2e10",     'res': True},
    {'str': " -90e3",   'res': True},
    {'str': " 1e",      'res': False},
    {'str': "e3",       'res': False},
    {'str': " 6e-1",    'res': True},
    {'str': " 99e2.5 ", 'res': False},
    {'str': "53.5e93",  'res': True},
    {'str': " --6 ",    'res': False},
    {'str': "-+3",      'res': False},
    {'str': "95a54e53", 'res': False},
    {'str': "3.",       'res': True}
]

# Solution 1: Regexp for valid number
p = re.compile(r'\s*[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?\s*$')

# Solution 2: Deterministic Finite Automaton or State Machine
transitions = [
    {'digit': 1, 'space': 0, 'sign': 5, 'dot': 3, 'exp': 9, 'other': 9},    # state 0
    {'digit': 1, 'space': 8, 'sign': 9, 'dot': 2, 'exp': 4, 'other': 9},    # state 1
    {'digit': 2, 'space': 8, 'sign': 9, 'dot': 9, 'exp': 4, 'other': 9},    # state 2
    {'digit': 2, 'space': 9, 'sign': 9, 'dot': 9, 'exp': 9, 'other': 9},    # state 3
    {'digit': 7, 'space': 9, 'sign': 6, 'dot': 9, 'exp': 9, 'other': 9},    # state 4
    {'digit': 1, 'space': 9, 'sign': 9, 'dot': 3, 'exp': 9, 'other': 9},    # state 5
    {'digit': 7, 'space': 9, 'sign': 9, 'dot': 9, 'exp': 9, 'other': 9},    # state 6
    {'digit': 7, 'space': 8, 'sign': 9, 'dot': 9, 'exp': 9, 'other': 9},    # state 7
    {'digit': 9, 'space': 8, 'sign': 9, 'dot': 9, 'exp': 9, 'other': 9},    # state 8
    # state 9 - error
]

for n in numbers:
    state = 0

    for symbol in n['str']:
        if state == 9: # Wrong symbol met
            break

        elif symbol >= '0' and symbol <= '9':
            condition = 'digit'
        elif symbol == '.':
            condition = 'dot'
        elif symbol in ['e', 'E']:
            condition = 'exp'
        elif symbol is ' ':
            condition = 'space'
        elif symbol in ['-', '+']:
            condition = 'sign'
        else:
            condition = 'other'

        print ('state {} condition {}'.format(state, condition))

        state = transitions[state][condition]

    smres = False # State Machine result
    reres = False # Regexp matching result

    if p.match(n['str']):
        reres = True

    if state in [1, 3, 7, 8]: # Valid Number End State
        smres = True

    print('Number "{}": \tregexp = {}, \tSM = {}, \tExpected = {}'\
        .format(n['str'], reres, smres, n['res']))


