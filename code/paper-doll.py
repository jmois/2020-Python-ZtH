def paper_doll(text):
    longtext = ''

    for char in text:
        longtext += char*3

    print (longtext)

if __name__ == '__main__':
    paper_doll('Hello')
    paper_doll('Missisippi')


    #error s =/= x