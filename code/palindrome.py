def palindrome(s):
    s = s.replace(' ','')
    return s == s[::-1]


if __name__ == '__main__':
    print(palindrome('nurses run'))