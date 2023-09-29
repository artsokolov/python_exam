def checksum(payload: int) -> int:
    s = 0
    is_double = True
    while payload != 0:
        num = payload % 10
        if is_double:
            num = num * 2
            if num >= 10:
                num -= 9
        s += num
        is_double = not is_double
        payload = payload // 10

    if s % 10 == 0:
        return s

    return (s + (10 - (s % 10))) - s


print(checksum(123))
