
def old_macdonald(name):
    first = name[0]
    second = name[1:3]
    third = name[3]
    fourth = name[4:]
    print(first.upper() + second + third.upper() + fourth)


if __name__ == '__main__':
    old_macdonald('macdonald')