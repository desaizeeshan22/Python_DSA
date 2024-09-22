n, m = input().split()
n = int(n)
m = int(m)
grid = []
for i in range(n):
    grid.append(input())

mod = 10 ** 9 + 7

dp = [[-1 for _ in range(m)] for _ in range(n)]


def func(r, c):
    if min(r, c) < 0 or r >= n or c >= m or grid[r][c] == '#':
        return 0
    if dp[r][c] != -1:
        return dp[r][c]
    if r == n - 1 and c == m - 1:
        return 1
    ans = 0
    ans += func(r + 1, c)
    ans += func(r, c + 1)
    dp[r][c] = ans % mod
    return dp[r][c]


print(func(0, 0))
