n, w = map(lambda x: int(x), input().split(" "))
l = []
for i in range(n):
    l.append(list(map(lambda x: int(x), input().split(" "))))

dp = [[0] * (n + 1) for _ in range(w + 1)]
for i in range(1, w + 1):
    for j in range(1, n + 1):
        dp[i][j] = max(dp[i][j], dp[i][j - 1])
        if i - l[j - 1][0] >= 0:
            dp[i][j] = max(dp[i][j], dp[i - l[j - 1][0]][j - 1] + l[j - 1][1])

print(dp[w][n])
