def maxTotalReward(rewardValues):
    rewards = rewardValues
    rewards.sort()
    dp = [[-1 for i in range(4001)]] * 4001

    def max_reward(index, total):
        if index >= len(rewards):
            return 0
        res = 0
        if dp[index][total] != -1:
            return dp[index][total]
        if rewards[index] > total:
            res = rewards[index] + max_reward(index + 1, total + rewards[index])
        res = max(res, max_reward(index + 1, total))
        dp[index][total] = res
        return dp[index][total]

    return max_reward(0, 0)


print(maxTotalReward([1, 6, 4, 3, 2]))
