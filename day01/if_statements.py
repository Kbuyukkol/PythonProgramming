if True:
    print(('Python'))
    print(('Java'))

score = 70
if score > 60:
    pass

print(('Congrats'))

s = 'Hello World'

if 'H' and 'W' in s:
    print(s, 'has', 'H and W')

if score >= 60:
    print('passed')
else:
    print(('failed'))

age = 20
result = None
if age >= 21:
    result = 'Eligible'
else:
    result = 'Not Eligible'

# ternary
age = 26
result = 'Eligible' if age >= 21 else 'Not Eligible'
