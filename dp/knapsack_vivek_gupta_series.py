# Write your code here

# you can set your Template at profile settings [https://maang.in/profile/edit-profile]

tests = int(input())
for _ in range(tests):
    values, weights = [], []
    n, w = input().split()
    n = int(n)
    w = int(w)
    temp = 0
    for i in range(n):
        weight, val = input().split()
        val = int(val)
        weight = int(weight)
        temp += weight
        values.append(val)
        weights.append(weight)
    dp = [[-1 for i in range(temp + 1)] for _ in range(n)]


    def func(i, weight_taken):
        if i == n:
            return 0
        if dp[i][weight_taken] != -1:
            return dp[i][weight_taken]
        temp = 0
        if weight_taken + weights[i] <= w:
            temp = values[i] + func(i + 1, weight_taken + weights[i])
        temp = max(temp, func(i + 1, weight_taken))
        dp[i][weight_taken] = temp
        return dp[i][weight_taken]


    print(func(0, 0))
