def solution(keymap, targets):
    key_index = {}

    for keys in keymap:
        # print(keys)
        for i, key in enumerate(keys):
            pre = key_index.get(key, 0)
            if pre == 0 or pre > i + 1:
                key_index[key] = i + 1

    answer = []
    # print(key_index)
    for target in targets:
        # print(target)
        types = 0
        for t in target:
            index = key_index.get(t, 0)
            if index == 0:
                types = -1
                break

            types += index

        answer.append(types)

    return answer


print(solution(["ABACD", "BCEFD"], ["ABCD", "AABB"]))
