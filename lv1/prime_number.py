def solution(n):
    numbers = list(range(n))
    answer = 0
    for i in range(1, n):
        if numbers[i] == 0:
            continue
        answer += 1
        j = i
        while j < n:
            numbers[j] = 0
            j += i + 1


    return answer


print(solution(5))