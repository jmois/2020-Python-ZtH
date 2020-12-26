st = 'Print only the words that start with s in this sentence'
# code here "Use for, .split(), and if

def splitting(text):
    for word in text.split():
        if word[0] == 's' or word[0]=='S':
            print(word)




if __name__ == '__main__':
    st = 'Print only the words that start with s in this sentence'
    splitting(st)