class Solution:
    def countOfPairs(self, values):
        self.n = len(values)
        dp = [[[-1 for _ in range(51)] for _ in range(51)] for _ in range(self.n)]
        mod_val = int(1e9 + 7)

        def solve(index, v1, v2):
            if index >= self.n:
                return 1
            if dp[index][v1][v2] != -1:
                return dp[index][v1][v2]

            result = 0
            for i in range(v1, values[index] + 1):
                for j in range(v2, -1, -1):
                    if i + j == values[index]:
                        result += solve(index + 1, i, j)
                        result %= mod_val

            dp[index][v1][v2] = result
            return result

        return solve(0, 0, values[0])
