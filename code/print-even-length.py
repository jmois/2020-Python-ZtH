
def print_even_lenght(text):
    for word in text.split():
        if (len(word))%2 == 0:
            print('EVEN:', word)
        else:
            pass



if __name__ == '__main__':
    st = 'Print every word in this sentence that has an even number of letters. PRINT EVEN!'
    print_even_lenght(st)
