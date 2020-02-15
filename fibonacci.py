# Recursive


def solution(x):
    if x < 2:
        answer = x
    elif x >= 2:
        answer = solution(x - 2) + solution(x - 1)
    return answer


# Iterative


def solution(x):
    if x < 2:
        answer = x
    else:
        a = 0
        b = 1
        for i in range(x - 1):
            a, b = b, a + b
            answer = b
    return answer
