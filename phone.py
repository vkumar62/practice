#!/usr/bin/python3

# Print all strings possible for a phone number

def phone_to_str(ph, i, ntoc, s):
    if i == len(ph):
        print(s.upper())
        return

    while not ph[i].isdigit():
        #s += ph[i]
        s += ' '
        i += 1

    for c in ntoc[ph[i]]:
        s += c
        phone_to_str(ph, i+1, ntoc, s)
        s = s[:-1]

ntoc = {
        '2' : 'abc',
        '3' : 'def',
        '4' : 'ghi',
        '5' : 'jkl',
        '6' : 'mno',
        '7' : 'pqrs',
        '8' : 'tuv',
        '9' : 'wxyz',
        '0' : '0',
        '1' : '1'
        }

phone_to_str('408-439-8194', 0, ntoc, '')
