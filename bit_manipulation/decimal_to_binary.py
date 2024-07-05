from collections import deque


def decimal_to_binary(number):
    res = deque()
    while number != 0:
        res.appendleft(str(number % 2))
        number = number // 2
    return "".join(res)

print(decimal_to_binary(13))
