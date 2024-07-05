# 3186.
# Maximum  Total Damage With Spell Casting
# A
# magician
# has
# various
# spells.
#
# You
# are
# given
# an
# array
# power, where
# each
# element
# represents
# the
# damage
# of
# a
# spell.Multiple
# spells
# can
# have
# the
# same
# damage
# value.
#
# It is a
# known
# fact
# that if a
# magician
# decides
# to
# cast
# a
# spell
# with a damage of power[i], they cannot cast any spell with a damage of power[i] - 2, power[i] - 1, power[i] + 1, or power[i] + 2.
#
# Each
# spell
# can
# be
# cast
# only
# once.
#
# Return
# the
# maximum
# possible
# total
# damage
# that
# a
# magician
# can
# cast.
#
# Example
# 1:
#
# Input: power = [1, 1, 3, 4]
#
# Output: 6
#
# Explanation:
#
# The
# maximum
# possible
# damage
# of
# 6 is produced
# by
# casting
# spells
# 0, 1, 3
# with damage 1, 1, 4.
#
# Example
# 2:
#
# Input: power = [7, 1, 6, 6]
#
# Output: 13
#
# Explanation:
#
# The
# maximum
# possible
# damage
# of
# 13 is produced
# by
# casting
# spells
# 1, 2, 3
# with damage 1, 6, 6.
#


from collections import defaultdict


def maximumTotalDamage(power):
    unique_powers = sorted(list(set(power)))
    mp = defaultdict(int)
    for elem in power:
        mp[elem] += 1
    dp = {}

    def top_down_dp(index, mp, unique_powers):
        if index >= len(unique_powers):
            return 0
        if index in dp:
            return dp[index]
        res = top_down_dp(index + 1, mp, unique_powers)
        next_idx = index + 1
        while next_idx < len(unique_powers) and unique_powers[next_idx] - unique_powers[index] <= 2:
            next_idx += 1
        res = max(res, mp[unique_powers[index]] * unique_powers[index] + top_down_dp(next_idx, mp, unique_powers))
        dp[index] = res
        return dp[index]

    # Tabulation
    dp = [0 for i in range(len(unique_powers))]
    dp[len(unique_powers) - 1] = unique_powers[len(unique_powers) - 1] * mp[unique_powers[len(unique_powers) - 1]]
    for i in range(len(unique_powers) - 2, -1, -1):
        j = i + 1
        while j < len(unique_powers) and unique_powers[j] - unique_powers[i] <= 2:
            j += 1
        dp[i] = dp[i + 1]
        if j < len(unique_powers):
            dp[i] = max(dp[i], unique_powers[i] * mp[unique_powers[i]] + dp[j])
        else:
            dp[i] = max(dp[i], unique_powers[i] * mp[unique_powers[i]])
    return dp[0]

    """
    :type power: List[int]
    :rtype: int
    """
