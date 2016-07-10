import sys

# Time out occured

# if __name__ == '__main__':
#     T = int(sys.stdin.readline())
#     for _ in range(T):
#         N = int(sys.stdin.readline())
#         prod =0
#         palindrome = 0
#         for a in range(100, N):
#             for b in range(100, N):
#                 prod = a*b
#                 num = prod
#                 rev = 0
#                 while (num != 0):
#                     dig = num % 10;
#                     rev = rev * 10 + dig;
#                     num = num // 10;
#                 if num ==rev:
#                     if prod > palindrome:
#                         palindrome = prod
#         print(palindrome)


# Do the bruteforce backwards

def max_palindrone(n):
    for i in range(n-1,101100,-1): #Strictly less than N
        if str(i) == str(i)[::-1] and three_digit_product(i):
            return i
def three_digit_product(n):
    for i in range(100,1000):
        if n%i ==0 and n/i in range(100,1000):
            return True
    return False

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        if (N < 1000000):
            print(max_palindrone(N))