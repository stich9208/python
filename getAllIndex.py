def solution(L, x):
    answer = []
    if x not in L:
        answer.append(-1)
    else:
        z = 0
        while True:
            c = L[z:]
            if x not in c:
                break
            else:
                d = c.index(x)
                answer.append(d + z)
                z += d + 1
    return answer

