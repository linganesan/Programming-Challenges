import sys

if __name__ == '__main__':
    T = int(sys.stdin.readline())

    for _ in range(T):
        N = int(sys.stdin.readline())
        print(sum(i for i in range(3,N) if i%3==0 or i%5==0))