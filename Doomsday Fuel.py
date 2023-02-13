from fractions import Fraction
def prant(ls):
    for x in ls:
        print x


def LCM(ls):
    counter = 1
    baseLowest = ls[0]
    for x in ls:
        if x < baseLowest: baseLowest = x

    while True:
        lowest = baseLowest * counter

        for x in ls:
            if lowest % x != 0:break
        else:
            return lowest

        counter += 1

def standardize(ls):
    original = []
    for i, row in enumerate(ls):
        if sum(row) == 0 or sum(row) == row[i]:
            original.append("r")
        else:
            original.append("t")

    new = [x for x in original if "t" in x]
    new.extend([x for x in original if "r" in x])

    if original != new:
        swap = {}
        for i in range(len(new)):
            if original[i] != "t" and not i >= new.count("t") + len(swap):
                swap[i] = new.count("t") + len(swap)

        for i, v in reversed(swap.items()):
            temp = [x for x in ls[i]]
            ls[i] = [x for x in ls[v]]
            ls[v] = [x for x in temp]

            for rows in range(len(ls)):
                temp2 = ls[rows][i]
                ls[rows][i] = ls[rows][v]
                ls[rows][v] = temp2

    for i in range(new.count("r")):
        ls[-(i + 1)][-(i + 1)] = 1

    for i, ival in enumerate(ls):
        total = sum(ival)
        for j, jval in enumerate(ival):
            ls[i][j] = Fraction(jval, total)

    Q = []
    R = []
    for i, ival in enumerate(ls):
        if i == new.count("t"): break
        q = []
        r = []
        for j, jval in enumerate(ival):
            if j < new.count("t"):
                q.append(jval)
            else:
                r.append(jval)
        Q.append(q)
        R.append(r)

    return ls, Q, R

def inverse(ls):
    inversedQ = [[0 for i in range(len(ls))] for j in range(len(ls))]
    for i in range(len(ls)):
        inversedQ[i][i] = 1

    for cycle in range(len(ls)):
        temp = ls[cycle][cycle]
        counter = 1
        while temp == 0:
            temp1 = [x for x in ls[cycle]]
            ls[cycle] = [x for x in ls[cycle+counter]]
            ls[counter] = [x for x in temp1]

            temp2 = [x for x in inversedQ[cycle]]
            inversedQ[cycle] = [x for x in inversedQ[cycle + counter]]
            inversedQ[counter] = [x for x in temp2]

            temp = ls[cycle][cycle]
        for column in range(len(ls)):
            ls[cycle][column] = ls[cycle][column] / temp
            inversedQ[cycle][column] = inversedQ[cycle][column] / temp

        for row in range(len(ls)):
            if row == cycle: continue
            temp2 = ls[row][cycle]
            for column in range(len(ls)):
                ls[row][column] = ls[row][column] - (temp2 * ls[cycle][column])
                inversedQ[row][column] = inversedQ[row][column] - (temp2 * inversedQ[cycle][column])

    return inversedQ

def solution(m):
    if len(m) == 1:
        return [1,1]
    ls, Q, R = standardize(m)

    I = [[0 for x in Q] for x in Q]
    for i in range(len(Q)):
        I[i][i] = 1

    for i in range(len(Q)):
        for j in range(len(Q)):
            I[i][j] = I[i][j] - Q[i][j]

    M = inverse(I)

    probabilities = []

    for i in range(len(R[0])):
        probability = 0
        for j in range(len(Q)):
            probability += M[0][j] * R[j][i]
        probabilities.append(probability)

    probdenom = [x.denominator for x in probabilities]
    denom = LCM(probdenom)

    answer = [int(x * denom) for x in probabilities]
    answer.append(denom)

    return answer
