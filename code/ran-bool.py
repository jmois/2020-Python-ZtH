def ran_bool(num,low,high):
    if num <= low or num >= high:
        return False
    else:
        return True


if __name__ == '__main__':
    print(ran_bool(5, 2, 7))