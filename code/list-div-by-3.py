# Use a list comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
def list_dev_by_3():
    lista = []
    for num in range (1,50):
        if num % 3 == 0:
            lista.append(num)
    return lista
if __name__ == '__main__':
    print(list_dev_by_3())