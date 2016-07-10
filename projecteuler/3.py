import sys

def calLargePrime(arg):
    V = int(arg)
    i = 2
    while i * i <= V:
        if V % i:
            i += 1
        else:
            V //= i
    return V

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        print(calLargePrime(N))