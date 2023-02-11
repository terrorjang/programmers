def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        root = int(i ** (1/2))
        if root ** 2 == i:
            answer -= i
        else:
            answer += i
    return answer

print(solution(13, 17))