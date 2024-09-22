def minimumCost(target, words, costs):
    end = '$'
    root = {}

    def insert(node, word, cost):
        curr = node
        for i in range(len(word)):
            char = word[i]
            if char not in curr:
                curr[char] = {}
            curr = curr[char]
            if i == len(word) - 1:
                curr[end] = min(curr.get(end, float("inf")), cost)

    for i in range(len(words)):
        insert(root, words[i], costs[i])

    def dp(idx):
        if idx >= len(target):
            return 0
        res = float("inf")
        curr = root
        for i in range(idx, len(target)):
            if target[i] not in curr:
                break
            curr = curr[target[i]]
            if '$' in curr:
                res = min(res, dp(i + 1) + curr['$'])
        return res

    ans = dp(0)
    return ans if ans != float("inf") else -1


print(minimumCost("abcdef", ["abdef", "abc", "d", "def", "ef"], [100, 1, 1, 10, 5]))
