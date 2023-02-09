def solution(s, skip, index):
    a = ord("a")
    z = ord("z")
    a_to_z = [i for i in range(a, z + 1)]

    for sk in skip:
        a_to_z.remove(ord(sk))

    length = len(a_to_z)

    answer = ""
    for c in s:
        print(c)
        _c = ord(c)
        i = a_to_z.index(_c)
        i = (i + index) % length
        answer += chr(a_to_z[i])

    return answer


print(solution("aukks", "wbqd", 5))
