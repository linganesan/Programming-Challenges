import sys
def calSmallestNum(arg):
    V = int(arg)
    primelist = []
    i = 2
    while i * i <= V:
        if V % i:
            primelist.append(i)
            i += 1
        else:
            V //= i

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        print(calSmallestNum(N))