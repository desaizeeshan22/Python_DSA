def func(A, B):
    if (len(B) > len(A)):
        return 0
    dp = [[0] * len(B) + 1 for _ in range(len(A) + 1)]
    for i in range(len(A) + 1):
        dp[i][0] = 1
    for i in range(len(A) + 1):
        for j in range(len(B) + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[len(A)][len(B)]
