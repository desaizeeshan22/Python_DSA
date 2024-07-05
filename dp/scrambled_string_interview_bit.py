dp = {}


def func(s1, s2):
    key = s1 + '-' + s2
    if key in dp:
        return dp[key]
    if s1 == s2:
        dp[key] = True
        return True
    if len(s1) != len(s2):
        dp[key] = False
        return False
    for i in range(1, len(s1)):
        dont_swap = func(s1[:i], s2[:i]) and func(s1[i:], s2[i:])
        swap = func(s1[:i], s2[len(s2) - i:]) and func(s1[i:], s2[:len(s2) - i])
        if dont_swap or swap:
            dp[key] = True
            return dp[key]
    dp[key] = False
    return dp[key]
