# list comprehension
def F_Letters(text):
    lista = []
    for word in text.split():
        lista.append(word[0])
    return lista




if __name__ == '__main__':
    st = 'Create a list of the first letters of every word in this string'
    print(F_Letters(st))