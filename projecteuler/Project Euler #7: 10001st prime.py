import sys
import math

def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def getPrime(arg):
    N = int(arg)
    primelist = [2,3]
    len = 2
    a = 5
    while len < N:
        if is_prime(a):
            primelist.append(a)
            len += 1
        a+=2
    return primelist.pop(N-1)

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        if N == 1:
            print(2)
        elif N ==2:
            print(3)
        else:
            print(getPrime(N))
