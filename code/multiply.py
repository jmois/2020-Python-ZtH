def multiply(numbers):
    total = 1
    for num in numbers:
        total = total * num
    return total


if __name__ == '__main__':
    print(multiply([1,2,3,-4,10]))