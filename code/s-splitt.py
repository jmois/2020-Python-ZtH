def s_split(text):
    for word in text.split():
        if word[0] == 's' or word[0]=='S':
            print(word)




if __name__ == '__main__':
    s_split('Sam Print only the words that start with s in this sentence')