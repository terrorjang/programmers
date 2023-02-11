def get_gcd(n, m):
    if m == 0:
        return n
    
    return get_gcd(m, n%m)

def solution(n, m):
    gcd = get_gcd(n, m)
    lcm = int( n*m/gcd)

    return [gcd, lcm]


print(solution(1,10))