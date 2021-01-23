def replace_to_ascii(line):
    replaced = ''

    for symbol in line:
        replaced += str(ord(symbol)) if '0' <= symbol <= '9' else symbol

    return replaced


samples = [
    'She loves 69',
    'I have called my 2 chicks',
    'There is the most shameless girl of the rest 228'
]

for s in samples:
    print(replace_to_ascii(s))
