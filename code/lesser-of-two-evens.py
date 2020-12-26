def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        if a > b:
            x = a
        else:
            x = b

    else:
        if a > b:
            x =  a
        else:
            x = b
    print(x)
pass

if __name__ == '__main__':
    lesser_of_two_evens(2,4)
    lesser_of_two_evens(2,5)
