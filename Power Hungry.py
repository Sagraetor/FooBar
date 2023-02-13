def solution(xs):
    indexOfFirstPos = 0
    for i in xs:
        if i >= 0:
            indexOfFirstPos = xs.index(i)
            break

    NegativeInts = []
    MaxProduct = xs.pop(indexOfFirstPos)

    for Ints in xs:
        # if MaxProduct == 0:
        #     MaxProduct = 1

        if Ints < 0:
            NegativeInts.append(Ints)
        elif Ints > 0:
            MaxProduct *= Ints

    NegativeInts.sort()

    if (len(NegativeInts) % 2 == 0 and MaxProduct < 0) or (len(NegativeInts) % 2 != 0 and MaxProduct > 0):
        NegativeInts = [x * -1 for x in NegativeInts[:-1]]

    for Ints in NegativeInts:
        MaxProduct *= Ints
    return str(MaxProduct)

print solution([-1, -2])