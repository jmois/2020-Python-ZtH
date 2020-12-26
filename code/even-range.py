# Use range() to print all the even numbers from 0 to 10
def even_range():
    i = 0
    while i < 10:
        if i%2 == 0:
            print(i)
            i+=1
        else:
            i+=1
            pass


if __name__ == '__main__':
    even_range()