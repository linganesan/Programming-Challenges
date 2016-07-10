import sys
import math
def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def calSmallestNum(arg):
    N = int(arg)
    primelist = [2,3]
    # only need to test odd numbers
    for x in range(5,N+1,2):
        if is_prime(x):
            primelist.append(x)
    newlist = []
    for a in primelist:
        i = 1
        while (a**i<=N):
            i += 1
            b = a**(i-1)
        newlist.append(b)
    result = 1
    for a in newlist:
        result *= a
    return result

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        if N == 2:
            print(2)
        elif N ==1:
            print(1)
        else:
            print(calSmallestNum(N))
