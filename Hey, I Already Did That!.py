def solution(n, b):
    cycle = []

    while True:
        cycle.append(n)
        number = [int(x) for x in str(n)]
        number.sort(reverse=True)
        x = number[:]
        number.sort()
        y = number[:]

        for i in range(1, len(number)+1):
            if x[-i] < y[-i]:
                x[-i-1] -= 1
                x[-i] += b
        z = []
        for i in range(len(x)):
            z.append(x[i]-y[i])

        zString = [str(x) for x in z]
        n = "".join(zString)
        n = int(n)

        if n in cycle:
            return len(cycle) - cycle.index(n)


print(solution(1211, 10))