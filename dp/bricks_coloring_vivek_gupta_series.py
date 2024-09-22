tests = int(input())
for _ in range(tests):
    n, m, k = input().split()
    n = int(n)
    m = int(m)
    k = int(k)
    colors = [i for i in range(m)]

    dp = [[[-1 for _ in range(n)] for _ in range(m)] for _ in range(n)]


    def func(i, prev_color, positions):
        if i == n:
            if positions == k:
                return 1
            return 0
        if positions > k:
            return 0
        temp = 0
        if dp[i][prev_color][positions] != -1:
            return dp[i][prev_color][positions]
        for color in colors:
            if color != prev_color and i > 0:
                temp += func(i + 1, color, positions + 1)
            else:
                temp += func(i + 1, color, positions)
        dp[i][prev_color][positions] = temp
        return dp[i][prev_color][positions]


    print(func(0, 0, 0))
