import sys

def calDiff(arg):
    N = int(arg)
    return overallSquare(N)-individualSquare(N)

def overallSquare(arg):
    sum = 0
    for i in range(1,N+1):
        sum += i
    return sum*sum

def individualSquare(N):
    sum = 0
    for i in range(1,N+1):
        sum += i*i
    return sum
    
if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        print(calDiff(N))