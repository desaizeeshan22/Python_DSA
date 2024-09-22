n = int(input())
act = []
for i in range(n):
    temp = [int(elem) for elem in input().split(" ")]
    act.append(temp)

dp = [[0] * 3 for _ in range(n)]
for j in range(3):
    dp[0][j] = act[0][j]
for i in range(1, n):
    for curr in range(3):
        for prev in range(3):
            if curr != prev:
                dp[i][curr] = max(dp[i][curr], act[i][curr] + dp[i - 1][prev])
res = 0
for elem in dp[n - 1]:
    res = max(res, elem)
print(res)
