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
    len = 1
    for x in range(5,10000,2):
        if len < N:
            if is_prime(x):
                primelist.append(x)
                len += 1
        else:
            break

    count = primelist.__len__()
    return primelist.pop(count-1)

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
