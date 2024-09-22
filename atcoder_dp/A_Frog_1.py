n = int(input())
arr = [int(elem) for elem in input().split(" ")]

dp = [float("inf")] * (n)
dp[n - 1] = 0
for i in range(n - 2, -1, -1):
    if i + 1 < n:
        dp[i] = min(dp[i], dp[i + 1] + abs(arr[i + 1] - arr[i]))
    if i + 2 < n:
        dp[i] = min(dp[i], dp[i + 2] + abs(arr[i + 2] - arr[i]))
print(dp[0])
# def frog(index, n, arr, dp):
#     if index >= n - 1:
#         return 0
#     res = float("inf")
#     if (dp[index] != -1):
#         return dp[index]
#     if index + 1 < n:
#         res = min(res, abs(arr[index] - arr[index + 1]) + frog(index + 1, n, arr, dp))
#     if index + 2 < n:
#         res = min(res, abs(arr[index] - arr[index + 2]) + frog(index + 2, n, arr, dp))
#     dp[index] = res if res != float("inf") else 0
#     return dp[index]


# print(frog(0, n, arr, defaultdict(lambda: -1)))
