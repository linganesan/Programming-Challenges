import sys

def calSum(arg):
    a = 1
    b = 2
    sum = a + b
    evensum = 2
    while(sum<=int(arg)):
        a = sum
        sum = b + sum
        b = a
        if (b%2 == 0):
            evensum += b
    return evensum

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        print(calSum(N))