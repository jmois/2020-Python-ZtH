def ran_check(num,low,high):
    if num <= low or num >= (high+1):
        return (f'{num} is not in the range between {low} and {high}')
    else:
        return (f'{num} is in the range between {low} and {high}')



if __name__ == '__main__':
    print(ran_check(5,2,7))