def makes_twenty(n1,n2):
    if n1 == 20 or n2 == 20:
        x = True
    elif n1 + n2 == 20:
        x = True
    else:
        x = False
    print(x)



if __name__ == '__main__':
    makes_twenty(20, 10)
    makes_twenty(12, 8)
    makes_twenty(2, 3)