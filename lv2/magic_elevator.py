def solution(storey):
    answer = 0
    while storey > 0:
        n = storey % 10
        storey //= 10
        if n < 5:
            answer += n
        elif n == 5:
            if storey % 10 >= 5:
                storey += 1
            answer += n
        else:
            answer += 10 - n
            storey += 1


    return answer


print(solution(16))
