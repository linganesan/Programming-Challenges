import sys

# https://codereview.stackexchange.com/questions/2/project-euler-problem-1-in-python-multiples-of-3-and-5
def sum_factors_of_n_below_k(k, n):
    m = (k-1) // n
    return n * m * (m+1) // 2

def calSum(arg):
    N = int(arg)
    return (sum_factors_of_n_below_k(N, 3) +
            sum_factors_of_n_below_k(N, 5) -
            sum_factors_of_n_below_k(N, 15))
if __name__ == '__main__':
    T = int(sys.stdin.readline())

    for _ in range(T):
        N = int(sys.stdin.readline())
        print(calSum(N))

# method1
# print(sum(i for i in range(3,N) if i%3==0 or i%5==0))


# method2
# def cal(limit):
#     s1, s2 = set(range(0, limit, 3)), set(range(0, limit, 5))
#     return sum(s1.union(s2))
#
# if __name__ == '__main__':
#     T = int(sys.stdin.readline())
#
#     for _ in range(T):
#         N = int(sys.stdin.readline())
#         print(cal(N))