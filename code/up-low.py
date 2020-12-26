def up_low(s):
    uppercase = 0
    lowercase = 0
    for char in s:
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1
        else:
            pass

    print(f"Original String: {s}")
    print(f'Uppercase count: {uppercase}')
    print(f'Lowercase count: {lowercase}')
if __name__ == '__main__':
    s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
    up_low(s)