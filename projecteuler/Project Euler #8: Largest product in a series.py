import sys

def calGreatestProduct(arg1,arg2,arg3):
    numlist = arg1
    K = int(arg2)
    N = int(arg3)
    b = 0
    for i in range(0,N-K+1):
        newlist = numlist[i:i+K]
        a = 1
        for n in newlist:
            a *= n
        if a > b:
            b = a
    return b
if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for _ in range(T):
        N,K = sys.stdin.readline().split(' ')
        num = int(sys.stdin.readline())
        stringnum = str(num)
        numlist = []
        for digit in stringnum:
            numlist.append (int(digit))
        print(calGreatestProduct(numlist,K,N))