def up_low(s):
    d = {'upper': 0, 'lower':0}
    for char in s:
        if char.isupper():
            d['upper'] += 1
        elif char.islower():
            d['lower'] += 1
        else:
            pass

    print(f"Original String: {s}")
    print(f'Uppercase count: {d["upper"]}')
    print(f'Lowercase count: {d["lower"]}')
if __name__ == '__main__':
    s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
    up_low(s)