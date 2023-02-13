def Fakesolution(n):
    n = int(n)
    binaryn = 0
    binaryn += n % 2
    while n != 0:
        count = 0
        n //= 2
        binaryn += 10^n

def solution(n):
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        elif n == 3 or n % 4 == 1:
            n = n - 1
        else:
            n = n + 1
        count += 1
    return count