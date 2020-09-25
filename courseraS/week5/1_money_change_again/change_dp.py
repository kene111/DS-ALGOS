# Uses python3
import sys

def get_change(money):
    #write your code here
    coins = [1,3,4]
    mon =  money + 1
    minnumcoins = [0] * mon
    minnumcoins[0] = 0

    for m in range(1,mon):
        minnumcoins[m] = mon
        for i in range(len(coins)):
            if m >= coins[i]: 
                newcoins =  minnumcoins[m-coins[i]] + 1
                if newcoins < minnumcoins[m]:
                    minnumcoins[m] = newcoins
    
    #print(minnumcoins)

    return minnumcoins[money]

if __name__ == '__main__':
    money = int(input())#sys.stdin.read())
    print(get_change(money))
