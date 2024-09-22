from collections import defaultdict

n, m = input().split()
n = int(n)
m = int(m)
dp = [0] * (n + 1)
d = defaultdict(list)
visited = [False] * (n + 1)
for i in range(m):
    u, v = input().split()
    u = int(u)
    v = int(v)
    d[u].append(v)


def dfs(node):
    visited[node] = True
    for neighbor in d[node]:
        if not visited[neighbor]:
            dfs(neighbor)
        dp[node] = max(dp[node], dp[neighbor] + 1)


for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
print(max(dp))
