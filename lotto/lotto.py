__author__ = 'jerrick'

import random

def makeLotto():
    numList = list(range(1, 47))
    random.shuffle(numList)
    # print(numList)
    return (numList[0:6], numList[6])

def main():
    lottoList = makeLotto()
    print("6 lotto number : ", lottoList[0])
    print("number for Second : ", lottoList[1])
if __name__ == '__main__':
    main()