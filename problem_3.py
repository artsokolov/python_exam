def solution(s: str) -> str:
    s_len = len(s)
    mid = s_len // 2

    if s_len % 2 == 0:
        return s[mid - 1] + s[mid]

    return s[mid]


print(solution('test'))
print(solution('testing'))
print(solution('middle'))
print(solution('t'))