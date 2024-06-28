# (:=) implemented in Python 3.8

txt = 'heelllooooooo'
if len(txt) > 10:
    print(f'too long: {len(txt)} elements')

if (n := len(txt)) > 10:
    print(f'too long: {n} elements')

while (n := len(txt)) > 1:
    print(n)
    txt = txt[:-1]
print(txt)
