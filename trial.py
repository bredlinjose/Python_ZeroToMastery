import os

locatorsPath = os.path.abspath

st = "hypen-of-hell"
for cha in st:
    if cha != '-':
        print(cha, end='')

for cha in st:
    if cha == '-':
        print(cha, end='')

