n = int(input())
inp = input().split()
p = [float(elem) for elem in inp]

dp = [[0.0] * (n + 1) for _ in range(n + 1)]

vis = [[False] * (n + 1) for _ in range(n + 1)]


def func(i, heads):
    if i == n + 1:
        tails = n - heads
        return 1.0 if heads > tails else 0.0
    if vis[i][heads]:
        return dp[i][heads]
    ans = (p[i - 1]) * func(i + 1, heads + 1)
    ans += (1 - p[i - 1]) * func(i + 1, heads)
    dp[i][heads] = ans
    vis[i][heads] = True
    return ans


print(func(1, 0))

