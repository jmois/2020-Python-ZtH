def blackjack(a,b,c):
    sum = a +b + c
    if sum <= 21:
        print(sum)
    elif sum >= 21 and (a == 11 or b == 11 or c == 11):
        print(sum -10)
    elif sum > 21:
        print('BUST')

if __name__ == '__main__':
    blackjack(5,6,7)
    blackjack(9,9,9)
    blackjack(9,9,11)