# L = list
# x = element


def solution(L, x):
    if x not in L:
        answer = -1
    else:
        i = L.index(x)
        upper = len(L) - 1
        lower = 0
        while upper >= lower:
            get = (upper + lower) // 2
            if get == i:
                answer = get
                break
            elif get > i:
                upper = get
                L = L[lower:upper]
            elif get < i:
                lower = get + 1
                L = L[lower:upper]
    return answer
