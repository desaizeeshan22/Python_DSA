def func(A, B):
    dp = [[-1 for _ in range(len(B))] for _ in range(len(A))]

    def solve(i, j, A, B, dp):
        if i < 0 and j < 0:
            return 0
        elif i < 0:
            return j + 1
        elif j < 0:
            return i + 1
        if dp[i][j] != -1:
            return dp[i][j]
        res = 0
        if A[i] == B[j]:
            res = solve(i - 1, j - 1, A, B, dp)
            dp[i][j] = res
            return dp[i][j]
        else:
            res = min(solve(i - 1, j, A, B, dp), solve(i, j - 1, A, B, dp))
            res = min(res, solve(i - 1, j - 1, A, B, dp))
            res += 1
            dp[i][j] = res
            return dp[i][j]
    return solve(len(A) - 1, len(B) - 1, A, B, dp)
