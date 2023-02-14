def solution(n):
    if n == 1 or n == 2:
        return n
    answer = n + 1
    m = int(n ** 0.5)
        
    for i in range(2, m + 1):
        if i * i == n:
            answer += i
            continue
        if n % i == 0:
            answer += i
            answer += (n // i)
            
        
    return answer

print(solution(12))