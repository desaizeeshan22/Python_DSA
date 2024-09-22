s = input()
t = input()
dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
for i in range(1, len(s) + 1):
    for j in range(1, len(t) + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        if s[i - 1] == t[j - 1]:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
ans = ""
i = len(s)
j = len(t)
temp = dp[i][j]
while temp > 0:
    if s[i - 1] == t[j - 1] and dp[i][j] > dp[i - 1][j] and dp[i][j] > dp[i][j - 1]:
        ans += s[i - 1]
        i -= 1
        j -= 1
        temp -= 1
    elif dp[i - 1][j] > dp[i][j - 1]:
        i -= 1
    else:
        j -= 1
print(ans[::-1])
