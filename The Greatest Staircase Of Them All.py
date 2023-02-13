# def solution(n):
#     currentStair = []
#     stairCount = 0
#     searching = True
#
#     currentStair.append(n-1)
#     currentStair.append(1)
#
#
#     while searching:
#         stairCount += 1
#         print currentStair
#         found = False
#
#         for i in range(len(currentStair)):
#             if i == 0: continue
#
#             if found: break
#
#             if (currentStair[i]) < (currentStair[i - 1] - 1):
#                 for j in range(len(currentStair)):
#                     if j <= i - 1: continue
#
#                     if (currentStair[j] + 1) < (currentStair[j - 1] - 1) and not found:
#                         currentStair[j] += 1
#                         currentStair[i - 1] -= 1
#                         found = True
#
#                     if currentStair[j] == currentStair[-1] and currentStair[j] >= 2:
#                         otherpossibles = 0
#                         while (currentStair[i - 1] - otherpossibles) > currentStair[j] > otherpossibles:
#                             otherpossibles += 1
#
#
#                         print "we detected ", otherpossibles, " more possibilities"
#                         stairCount += otherpossibles
#
#             if currentStair[i] == currentStair[-1] and currentStair[i] >= 3 and not found:
#                 currentStair[i] -= 1
#                 currentStair.append(1)
#
#             elif currentStair[i] == currentStair[-1] and not found:
#                 searching = False
#                 break
#
#     return stairCount
#
# print solution(12)

def solution(n):
    currentEquation = [0] * (n + 1)
    currentEquation[0] = 1
    currentEquation[1] = 1
    for i in range(n):
        result = [0] * (n + 1)
        newEquation = [0] * (n + 2)
        newEquation[0] = 1
        newEquation[i+2] = 1
        for power, coefficient in enumerate(currentEquation):
            for power2, coefficient2 in enumerate(newEquation):
                # print power, power2, power+power2
                # print coefficient, coefficient2, coefficient * coefficient2
                # print newEquation
                # print currentEquation
                if power+power2 > len(currentEquation) - 1:
                    continue
                result[power+power2] += (coefficient * coefficient2)
        currentEquation = result
    return (currentEquation[-1]-1)

print solution(200)

# (1+x)(1+x2)(1+x3)
#
#
#
#
#
#
##