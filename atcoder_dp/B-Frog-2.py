input_list = [int(elem) for elem in input().split(" ")]
n, k = input_list[0], input_list[1]
arr = [int(elem) for elem in input().split(" ")]

dp = [float("inf")] * n
dp[0] = 0
for i in range(1, n):
    for j in range(max(i - k, 0), i):
        dp[i] = min(dp[i], dp[j] + abs(arr[j] - arr[i]))
print(dp[n - 1])
