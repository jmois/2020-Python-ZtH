
def square(num):
    return num**2


if __name__ == '__main__':
    my_nums = [1,2,3,4,5]
    for item in map(square,my_num):
        print(item)

list(map(square,my_num))