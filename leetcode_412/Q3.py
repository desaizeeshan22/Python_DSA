import heapq


def getFinalState(nums, k, multiplier):
    heap = [elem for elem in nums]
    temp = {v: i for i, v in enumerate(nums)}
    res = [0] * len(nums)
    for i in range(k):
        e = min(nums)
        idx = temp[e]
        nums[idx] = e * multiplier

    return res

    """
    :type nums: List[int]
    :type k: int
    :type multiplier: int
    :rtype: List[int]
    """


print(getFinalState([2, 1, 3, 5, 6], 5, 2))
