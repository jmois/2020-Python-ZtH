def animal_crackers(text):
    mylist = text.split(' ')
    y = [x[0] for x in mylist]
    if y[0] == y[1]:
        x = True
    else:
        x = False
    print(x)



if __name__ == '__main__':
    animal_crackers('Levelhead Llama')
    animal_crackers('Crazy Kangaroo')